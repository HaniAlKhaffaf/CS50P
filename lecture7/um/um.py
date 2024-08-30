import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    if matches:
        return len(matches) 
    else:
        return 0


if __name__ == "__main__":
    main()