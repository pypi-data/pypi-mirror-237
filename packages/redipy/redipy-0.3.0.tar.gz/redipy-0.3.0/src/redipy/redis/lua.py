import json
from collections.abc import Iterable
from typing import Literal, TYPE_CHECKING

from redipy.backend.backend import Backend, ExecFunction
from redipy.graph.cmd import CommandObj
from redipy.graph.expr import BinOps, CallObj, ExprObj, get_literal, JSONType
from redipy.graph.seq import SequenceObj
from redipy.plugin import (
    add_patch_plugin,
    add_plugin,
    HELPER_PKG,
    HelperFunction,
    LuaGeneralPatch,
    LuaRedisPatch,
)
from redipy.util import code_fmt, indent, json_compact, lua_fmt


if TYPE_CHECKING:
    from redipy.redis.conn import RedisConnection


class LuaFnHook:
    def __init__(
            self,
            helper_fns: dict[str, HelperFunction],
            general_patch_fns: dict[str, LuaGeneralPatch],
            redis_patch_fns: dict[str, LuaRedisPatch]) -> None:
        self._helpers: set[str] = set()
        self._helper_fns = helper_fns
        self._general_patch_fns = general_patch_fns
        self._redis_patch_fns = redis_patch_fns
        self._is_expr_stmt = False

    def set_expr_stmt(self, is_expr_stmt: bool) -> None:
        self._is_expr_stmt = is_expr_stmt

    def is_expr_stmt(self) -> bool:
        return self._is_expr_stmt

    def build_helpers(self) -> list[str]:
        res = []
        prefix = f"{HELPER_PKG}."
        for helper in sorted(self._helpers):
            short_name = helper.removeprefix(prefix)
            help_obj = self._helper_fns.get(short_name)
            if help_obj is None:
                raise RuntimeError(f"unknown helper {short_name}")
            res.append(f"function {helper} ({help_obj.args()})")
            res.extend(indent(lua_fmt(help_obj.body()), 2))
            res.append("end")
        return res

    def adjust_function(self, expr: CallObj, is_expr_stmt: bool) -> ExprObj:
        expr["no_adjust"] = True
        name = expr["name"]
        args = expr["args"]
        if name == "redis.call":
            r_name = get_literal(args[0], "str")
            if r_name is not None:
                return self.adjust_redis_fn(
                    expr, f"{r_name}", args[1:], is_expr_stmt=is_expr_stmt)
        patch_fn = self._general_patch_fns.get(name)
        if patch_fn is not None:
            return patch_fn.patch(expr, is_expr_stmt=is_expr_stmt)
        if name.startswith(f"{HELPER_PKG}."):
            self._helpers.add(name)
            return expr
        return expr

    def adjust_redis_fn(
            self,
            expr: CallObj,
            name: str,
            args: list[ExprObj],
            *,
            is_expr_stmt: bool) -> ExprObj:
        patch_fn = self._redis_patch_fns.get(name)
        if patch_fn is None:
            return expr
        return patch_fn.patch(expr, args, is_expr_stmt=is_expr_stmt)


def indent_str(code: Iterable[str], add_indent: int) -> list[str]:
    ind = " " * add_indent
    return [f"{ind}{exe}" for exe in code]


KEYV_HOOK = "--[[ KEYV"
ARGV_HOOK = "--[[ ARGV"
HOOK_END = "]]"


class LuaBackend(
        Backend[list[str], str, LuaFnHook, LuaFnHook, 'RedisConnection']):
    def __init__(self) -> None:
        super().__init__()
        self._helper_fns: dict[str, HelperFunction] = {}
        self._redis_patch_fns: dict[str, LuaRedisPatch] = {}
        self._general_patch_fns: dict[str, LuaGeneralPatch] = {}
        self.add_helper_function_plugin("redipy.redis.helpers")
        self.add_general_patch_plugin("redipy.redis.gpatch")
        self.add_redis_patch_plugin("redipy.redis.rpatch")

    def add_helper_function_plugin(self, module: str) -> None:
        add_plugin(module, self._helper_fns, HelperFunction)

    def add_general_patch_plugin(self, module: str) -> None:
        add_patch_plugin(
            module,
            self._general_patch_fns,
            LuaGeneralPatch,
            disallowed={"redis.call"})

    def add_redis_patch_plugin(self, module: str) -> None:
        add_patch_plugin(module, self._redis_patch_fns, LuaRedisPatch)

    def create_command_context(self) -> LuaFnHook:
        return LuaFnHook(
            self._helper_fns, self._general_patch_fns, self._redis_patch_fns)

    def finish(self, ctx: LuaFnHook, script: list[str]) -> list[str]:
        res = []
        helpers = ctx.build_helpers()
        if helpers:
            res.append("-- HELPERS START --")
            res.append(f"local {HELPER_PKG} = {{}}")
            res.extend(helpers)
            res.append("-- HELPERS END --")
        res.extend(script)
        return res

    def compile_sequence(self, ctx: LuaFnHook, seq: SequenceObj) -> list[str]:
        res = []
        if seq["kind"] == "script":
            key_order = seq["keyv"]
            arg_order = seq["argv"]
            res.append(KEYV_HOOK)
            for key in key_order:
                res.append(key)
            res.append(HOOK_END)
            res.append(ARGV_HOOK)
            for arg in arg_order:
                res.append(arg)
            res.append(HOOK_END)

        res.extend(indent_str(
            (
                exe
                for cmd in seq["cmds"]
                for exe in self.compile_command(ctx, cmd)
            ),
            0 if seq["kind"] == "script" else 2))
        return res

    def compile_command(self, ctx: LuaFnHook, cmd: CommandObj) -> list[str]:
        # FIXME: add debug context in comments
        if cmd["kind"] == "assign" or cmd["kind"] == "declare":
            is_declare = cmd["kind"] == "declare"
            decl = "local " if is_declare else ""
            rhs = self.compile_expr(ctx, cmd["value"])
            assign_obj = cmd["assign"]
            lcl_name = assign_obj["name"]
            if assign_obj["kind"] == "arg" or assign_obj["kind"] == "key":
                ext_name = f"  -- {assign_obj['readable']}"
            else:
                ext_name = ""
            return [f"{decl}{lcl_name} = {rhs}{ext_name}"]
        if cmd["kind"] == "assign_at":
            arr_ix = self.compile_expr(ctx, cmd["index"])
            rhs = self.compile_expr(ctx, cmd["value"])
            assign_obj = cmd["assign"]
            if assign_obj["kind"] == "var":
                lcl_name = assign_obj["name"]
                return [f"{lcl_name}[{arr_ix} + 1] = {rhs}"]
            raise ValueError(
                f"cannot assign to position of {cmd['assign']['kind']}")
        if cmd["kind"] == "stmt":
            ctx.set_expr_stmt(True)
            stmt = self.compile_expr(ctx, cmd["expr"])
            return [stmt]
        if cmd["kind"] == "branch":
            res = [f"if {self.compile_expr(ctx, cmd['condition'])} then"]
            res.extend(self.compile_sequence(ctx, cmd["then"]))
            elses = self.compile_sequence(ctx, cmd["else"])
            if elses:
                res.append("else")
                res.extend(elses)
            res.append("end")
            return res
        if cmd["kind"] == "for":
            assert cmd["index"]["kind"] == "index"
            assert cmd["value"]["kind"] == "var"
            res = [(
                f"for {cmd['index']['name']}, {cmd['value']['name']} "
                f"in ipairs({self.compile_expr(ctx, cmd['array'])}) do"
            )]
            res.extend(self.compile_sequence(ctx, cmd["body"]))
            res.append("end")
            return res
        if cmd["kind"] == "while":
            res = [f"while {self.compile_expr(ctx, cmd['condition'])} do"]
            res.extend(self.compile_sequence(ctx, cmd["body"]))
            res.append("end")
            return res
        if cmd["kind"] == "return":
            if cmd["value"] is None:
                return []
            return [
                f"return cjson.encode({self.compile_expr(ctx, cmd['value'])})",
            ]
        raise ValueError(f"unknown kind {cmd['kind']} for command {cmd}")

    def compile_expr(self, ctx: LuaFnHook, expr: ExprObj) -> str:
        is_expr_stmt = ctx.is_expr_stmt()
        if is_expr_stmt:
            ctx.set_expr_stmt(False)
        if expr["kind"] == "var":
            return expr["name"]
        if expr["kind"] == "arg":
            return expr["name"]
        if expr["kind"] == "key":
            return expr["name"]
        if expr["kind"] == "index":
            return f"({expr['name']} - 1)"
        if expr["kind"] == "load_json_arg":
            return f"cjson.decode(ARGV[{expr['index'] + 1}])"
        if expr["kind"] == "load_key_arg":
            return f"(KEYS[{expr['index'] + 1}])"
        if expr["kind"] == "val":
            val_type = expr["type"]
            value = expr["value"]
            if val_type == "bool":
                return f"{value}".lower()
            if val_type in ("int", "float"):
                return f"{value}"
            if val_type == "str":
                res = f"{value}"
                res = res.replace("\"", "\\\"").replace("\n", "\\n")
                return f"\"{res}\""
            if val_type == "list":
                res = json_compact(value).decode("utf-8")
                res = res.replace("\"", "\\\"").replace("\n", "\\n")
                return f"cjson.decode(\"{res}\")"
            if val_type == "none":
                return "nil"
            raise ValueError(f"unknown value type {val_type} for {expr}")
        if expr["kind"] == "unary":
            if expr["op"] == "not":
                return f"(not {self.compile_expr(ctx, expr['arg'])})"
            raise ValueError(f"unknown op {expr['op']} for {expr}")
        if expr["kind"] == "binary":
            ops: dict[BinOps, str] = {
                "and": "and",
                "or": "or",
                "add": "+",
                "sub": "-",
                "lt": "<",
                "le": "<=",
                "gt": ">",
                "ge": ">=",
                "eq": "==",
                "ne": "~=",
            }
            op = ops.get(expr["op"])
            if op is not None:
                return (
                    f"({self.compile_expr(ctx, expr['left'])} "
                    f"{op} "
                    f"{self.compile_expr(ctx, expr['right'])})")
            raise ValueError(f"unknown op {expr['op']} for {expr}")
        if expr["kind"] == "constant":
            return f"{expr['raw']}"
        if expr["kind"] == "array_at":
            return (
                f"{self.compile_expr(ctx, expr['var'])}"
                f"[{self.compile_expr(ctx, expr['index'])} + 1]")
        if expr["kind"] == "array_len":
            return f"#{self.compile_expr(ctx, expr['var'])}"
        if expr["kind"] == "concat":
            return " .. ".join(
                f"({self.compile_expr(ctx, strobj)})"
                for strobj in expr["strings"])
        if expr["kind"] == "call":
            if not expr["no_adjust"]:
                adj_expr = ctx.adjust_function(expr, is_expr_stmt)
                return self.compile_expr(ctx, adj_expr)
            argstr = ", ".join(
                self.compile_expr(ctx, arg) for arg in expr["args"])
            return f"{expr['name']}({argstr})"
        raise ValueError(f"unknown kind {expr['kind']} for expression {expr}")

    def create_executable(
            self,
            code: list[str],
            runtime: 'RedisConnection') -> ExecFunction:
        key_order = []
        arg_order = []
        mode: Literal["none", "keyv", "argv"] = "none"
        for line in code:
            ln = line.strip()
            if ln == HOOK_END:
                mode = "none"
                continue
            if ln == KEYV_HOOK:
                mode = "keyv"
                continue
            if ln == ARGV_HOOK:
                mode = "argv"
                continue
            if mode == "keyv":
                key_order.append(ln)
                continue
            if mode == "argv":
                arg_order.append(ln)
                continue
        compute = runtime.get_dynamic_script(code_fmt(code))

        def exec_code(
                keys: dict[str, str],
                args: dict[str, JSONType]) -> JSONType:
            with runtime.get_connection() as client:
                res = compute(
                    keys=[runtime.with_prefix(keys[key]) for key in key_order],
                    args=[json_compact(args[arg]) for arg in arg_order],
                    client=client)
            if res is None:
                return None
            # NOTE: it is impossible to distinguish between {} and [] in lua
            if res == br"{}":
                return None
            return json.loads(res)

        return exec_code
