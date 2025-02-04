import os
import subprocess
import sys
from typing import List, Optional, Tuple

from .helper import check_builtin_command, check_exists_dir, find_exec_path


def cmd_echo(cmd: str) -> None:
    try:
        # Check if the command is echo
        check = cmd.split(" ")[0] == "echo"
        if check:
            sys.stdout.write(f"{cmd.replace('echo ', '')}\n")
    except Exception as e:
        raise e
    return


def cmd_exit(cmd: str) -> None:
    try:
        # Check if the command is exit
        check = cmd.split(" ")[0] == "exit"
        if check:
            exit(0)
    except Exception as e:
        raise e


def cmd_type(cmd: str) -> None:
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


def pwd() -> str:
    try:
        curr_dir = os.getcwd()
        sys.stdout.write(f"{curr_dir}\n")
    except Exception as e:
        raise e
    return curr_dir


def cd(directory: str):
    try:
        # If the directory is absolute
        if directory.startswith("/"):
            # Check the new directory exists
            if not check_exists_dir(directory):
                return
            os.chdir(directory)
            return
        else:  # If the directory is relative
            # Get the current directory
            curr_dir = os.getcwd()
            dirs = directory.split("/")

            for element in dirs:
                if element == "..":
                    curr_dir = os.path.dirname(curr_dir)
                elif element == ".":
                    continue
                elif element == "~":
                    os.chdir(os.path.expanduser("~"))
                    return
                else:
                    curr_dir = os.path.join(curr_dir, element)

            # Check the new directory exists
            if not check_exists_dir(curr_dir):
                return

            # Change the directory
            os.chdir(curr_dir)
    except Exception as e:
        raise e
