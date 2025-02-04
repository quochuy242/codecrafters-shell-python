import os
import subprocess
import sys
from typing import List, Optional, Tuple

from .helper import check_builtin_command, check_exists_dir, find_exec_path
from .cmd import cmd_echo, cmd_exit, cmd_type, pwd, cd, run_program


def main():
    while True:
        user_input = input("$ ")
        command, *args = user_input.split(" ")

        # Check if the command is a shell builtin
        if check_builtin_command(command):
            if command == "echo":
                cmd_echo(user_input)
                continue
            if command == "exit":
                cmd_exit(user_input)
                continue
            if command == "type":
                cmd_type(user_input)
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
