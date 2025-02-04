import shlex
import os
import sys
from typing import List, Optional


def check_builtin_command(cmd: str) -> bool:
    builtin_cmds = ["echo", "exit", "type", "pwd", "cd"]
    res = True if cmd in builtin_cmds else False
    return res


def find_exec_path(cmd: str) -> Optional[str]:
    paths = os.environ.get("PATH").split(":")
    for path in paths:
        exec_path = os.path.join(path, cmd)
        if os.path.exists(exec_path):
            return exec_path
    return None


def check_exists_dir(path: str) -> bool:
    check = os.path.exists(path)
    if not check:
        sys.stdout.write(f"cd: {path}: No such file or directory\n")
    return check


def remove_unwanted_spaces(string: str) -> str:
    return " ".join(string.split())
