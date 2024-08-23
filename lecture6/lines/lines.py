import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many argumnts")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    file_name = sys.argv[1]
    count = 0
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                if checking_validity(line.strip()):
                    count = count + 1
        print(count)
    except FileNotFoundError:
        sys.exit(f"The file '{file_name}' does not exist.")


def checking_validity(line):
    if line == "" or line[0] == "#":
        return False
    else:
        return True






if __name__ == "__main__":
    main()