import sys


def main():
    while True:
        cmd = input("$ ")
        if cmd == "exit 0":
            return 0
        print(f"{cmd}: command not found")
  

if __name__ == "__main__":
    main()
