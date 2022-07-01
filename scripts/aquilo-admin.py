def execute_command(args: list) -> None:
    print("run command: " + " ".join(args))


if __name__ == '__main__':
    import sys

    sys.path.append('aquilo-admin')
    execute_command(sys.argv[1:])
    sys.exit(0)
