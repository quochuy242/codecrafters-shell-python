import sys
import shlex
from . import cmd, helper


def main():
    while True:
        user_input = input("$ ")
        command, *args = shlex.split(user_input)

        # Support redirecting output
        if ">" in args or "1>" in args:
            cmd.redirect_output(command, args)
            continue
        elif "2>" in args:
            cmd.redirect_output(command, args, error=True)
            continue

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
