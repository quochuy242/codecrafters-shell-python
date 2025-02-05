import os
import subprocess
import sys
from typing import Optional, List, Tuple


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


def capture_output(
    cmd: str, args: List[str], capture_stderr: bool = False
) -> Tuple[Optional[str], Optional[str]]:
    """Executes a command and captures both stdout and stderr."""
    full_cmd = f"{cmd} {' '.join(args)}"
    try:
        output = subprocess.run(
            full_cmd, shell=True, text=True, capture_output=True, check=True
        )
        return (
            output.stdout,
            output.stderr if capture_stderr else None,
        )  # stderr is None unless explicitly captured
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr  # Capture both outputs when an error occurs
