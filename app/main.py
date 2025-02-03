import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    cmd = input()
    if cmd == 'exit 0': 
        sys.exit(0)
    else:
        print(f'{cmd}: command not found')
        main()
  

if __name__ == "__main__":
    main()
