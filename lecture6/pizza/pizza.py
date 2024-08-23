import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many argumnts")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    file_name = sys.argv[1]
    final_result = table(file_name)
    print(final_result)

def table(file_name):
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            table = tabulate(reader, tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit(f"The file '{file_name}' does not exist.")

if __name__ == "__main__":
    main()