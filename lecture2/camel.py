def main():
    user_input = input("camelCase: ")
    print("snake_case: ", end="")
    for letter in user_input:
        if letter.isupper():
            letter = letter.lower()
            print("_", end="")
        print(letter, end="")

main()