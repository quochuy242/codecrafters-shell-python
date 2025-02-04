import os
import subprocess
import sys
from typing import List, Optional, Tuple


def handle_echo(cmd: str) -> None:
    try:
        # Check if the command is echo
        check = cmd.split(" ")[0] == "echo"
        if check:
            sys.stdout.write(f"{cmd.replace('echo ', '')}\n")
    except Exception as e:
        raise e
    return


def handle_exit(cmd: str) -> None:
    try:
        # Check if the command is exit
        check = cmd.split(" ")[0] == "exit"
        if check:
            exit(0)
    except Exception as e:
        raise e


def find_exec_path(cmd: str) -> Optional[str]:
    paths = os.environ.get("PATH").split(":")
    for path in paths:
        exec_path = os.path.join(path, cmd)
        if os.path.exists(exec_path):
            return exec_path
    return None


def check_builtin_command(cmd: str) -> bool:
    builtin_cmds = ["echo", "exit", "type", "pwd"]
    res = True if cmd in builtin_cmds else False
    return res


def handle_type(cmd: str) -> None:
    try:
        # Check if the command is type
        check = cmd.split(" ")[0] == "type"
        if not check:
            raise Exception("Not a type command\n")

        # Check if the command is valid and print the result
        content = cmd.replace("type ", "")
        builtin_check = check_builtin_command(
            content
        )  # Check if the command is a shell builtin
        exec_path = find_exec_path(content)  # Check if the command is an executable

        # Print the result
        if builtin_check:
            sys.stdout.write(f"{content} is a shell builtin\n")
        elif exec_path is not None:
            sys.stdout.write(f"{content} is {exec_path}\n")
        else:
            sys.stdout.write(f"{content}: not found\n")
    except Exception as e:
        raise e
    return


def run_program(program_name: str, args: List[str]):
    try:
        # Run the program
        subprocess.run([program_name, *args])
    except Exception as e:
        raise e


def pwd():
    try:
        curr_dir = os.getcwd()
        sys.stdout.write(f"{curr_dir}\n")
    except Exception as e:
        raise e
    return


def main():
    while True:
        user_input = input("$ ")
        command, *args = user_input.split(" ")

        # Check if the command is a shell builtin
        if check_builtin_command(command):
            if command == "echo":
                handle_echo(user_input)
                continue
            if command == "exit":
                handle_exit(user_input)
                continue
            if command == "type":
                handle_type(user_input)
                continue
            if command == "pwd":
                pwd()
                continue
        elif find_exec_path(command) is not None:
            run_program(program_name=command, args=args)
        else:
            sys.stdout.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
