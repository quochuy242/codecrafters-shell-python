import sys
import os 
from typing import List, Tuple, Optional

def check_builtin_command(cmd: str) -> bool:
    builtin_cmds = ["echo", 'exit', 'type']
    res = True if cmd in builtin_cmds else False
    return res

        
def check_exec_command(cmd: str) -> Tuple[bool, Optional[str]]:
    paths = os.environ.get("PATH").split(":")
    
    for path in paths:
        exec_path = f'{path}/{cmd}'
        if os.path.exists(exec_path):
            return True, exec_path
        
    return False, None
    

def main():
    while True:
        user_input = input("$ ")
        
        if user_input == "exit 0":
            break
        
        if user_input.split(' ')[0] == 'echo':
            sys.stdout.write(f'{user_input.replace("echo ", '')}\n')
            continue
        
        if user_input.split(' ')[0] == 'type':
            cmd = user_input.split(" ")[1]
            builtin_check = check_builtin_command(cmd)
            exec_check, exec_path = check_exec_command(cmd)
            if builtin_check:
                sys.stdout.write(f'{cmd} is a shell builtin\n')
            elif exec_check:
                sys.stdout.write(f'{cmd} is {exec_path}\n')
            else:
                sys.stdout.write(f'{cmd}: not found\n')
            continue
        
        sys.stdout.write(f"{user_input}: command not found\n")

if __name__ == "__main__":
    main()
