import os
import subprocess
import sys
from typing import List, Optional, Tuple

from .helpers import check_builtin_command, check_exists_dir, find_exec_path


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
            curr_dir = pwd()
            abs_dir = os.path.join(curr_dir, directory)

            # Check the new directory exists
            if not check_exists_dir(abs_dir):
                return

            # Change the directory
            os.chdir(abs_dir)
    except Exception as e:
        raise e


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
            if command == "cd":
                cd(args[0])
                continue
        elif find_exec_path(command) is not None:
            run_program(program_name=command, args=args)
        else:
            sys.stdout.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
