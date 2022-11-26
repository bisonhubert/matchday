import sys


def handle_stdin():
    print("in handle_stdin")
    print(sys.stdin.readlines())


def handle_filepath(filepath):
    print("in handle_filepath")
    print(filepath)


def main():
    print("in main")
    args = sys.argv[1:]
    if len(args) == 0:
        print("input via stdin")
        handle_stdin()
    else:
        print("input as a filepath")
        filepath = args[0]
        handle_filepath(filepath)


if __name__ == "__main__":
    main()
