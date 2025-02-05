import os
import subprocess
import sys
from typing import List

from . import helper


def run_echo(args: List[str]) -> None:
    try:
        # Print the result
        sys.stdout.write(f"{' '.join(args)}\n")
    except Exception as e:
        raise e
    return


def run_exit(args: List[str]) -> None:
    try:
        sys.exit(int(args[0]) if args else 0)
    except Exception as e:
        raise e


def run_type(args: List[str]) -> None:
    try:
        for arg in args:
            # Check if the command is valid and print the result
            builtin_check = helper.check_builtin_command(
                arg
            )  # Check if the command is a shell builtin
            exec_path = helper.find_exec_path(
                arg
            )  # Check if the command is an executable

            # Print the result
            if builtin_check:
                sys.stdout.write(f"{arg} is a shell builtin\n")
            elif exec_path is not None:
                sys.stdout.write(f"{arg} is {exec_path}\n")
            else:
                sys.stdout.write(f"{arg}: not found\n")
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
            if not helper.check_exists_dir(directory):
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
            if not helper.check_exists_dir(curr_dir):
                return

            # Change the directory
            os.chdir(curr_dir)
    except Exception as e:
        raise e


def redirect_output(cmd: str, args: List[str], error: bool = False) -> None:
    try:
        # Get the index of args containing ">"
        idx = next((i for i, arg in enumerate(args) if ">" in arg), 0)

        # Get the arguments after ">" and remove redirects args from args
        file = args[idx + 1]
        args = args[:idx]

        # Capture the output (stdout + stderr)
        main_output = helper.capture_output(cmd=cmd, args=args)

        # Ensure directory exists
        if os.path.dirname(file) != "":
            os.makedirs(os.path.dirname(file), exist_ok=True)
        
        if main_output is not None:
            with open(file, "w") as f:
                f.write(main_output)

    except Exception as e:
        sys.stderr.write(str(e) + "\n")
