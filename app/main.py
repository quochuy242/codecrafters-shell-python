import sys
from typing import List

from . import cmd, helper


def main():
    while True:
        user_input = input("$ ")
        try:
            command, args = user_input.split(" ", 1)
            args: List[str] = helper.extract_args(args)
        except ValueError:
            # If the input is just a command
            command = user_input
            args = []

        # Check if the command is a shell builtin
        if helper.check_builtin_command(command):
            if command == "echo":
                cmd.run_echo(args)
                continue
            if command == "exit":
                cmd.run_exit(args)
                continue
            if command == "type":
                cmd.run_type(args)
                continue
            if command == "pwd":
                cmd.pwd()
                continue
            if command == "cd":
                cmd.cd(args[0])
                continue
        elif helper.find_exec_path(command) is not None:
            cmd.run_program(program_name=command, args=args)
        else:
            sys.stdout.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
