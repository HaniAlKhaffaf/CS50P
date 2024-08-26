import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-255]+\.[0-255]+\.[0-255]+\.[0-255]+$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()