import sys

def check_builtin_command(cmd: str):
    builtin_cmds = ["echo", 'exit', 'type']
    if cmd in builtin_cmds:
        print(f'{cmd} is a shell builtin')
    else: 
        print(f"{cmd}: not found")

def main():
    while True:
        cmd = input("$ ")
        if cmd == "exit 0":
            return 0
        elif cmd[:4] == 'echo':
            print(cmd[5:])
        elif cmd[:4] == 'type':
            check_builtin_command(cmd[5:])
        else:
            print(f"{cmd}: command not found")
  

if __name__ == "__main__":
    main()
