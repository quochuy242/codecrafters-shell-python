import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    cmd = input()
    print(f'{cmd}: command not found\n')


if __name__ == "__main__":
    main()
