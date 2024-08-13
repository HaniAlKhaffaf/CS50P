def main():
    userInput = input("what is the answer to the Great Question of Life, the Universe and Everything?")
    match userInput:
        case "42":
            print("yes")
        case "forty-two":
            print("yes")
        case "forty two":
            print("yes")
        case _:
            print("no")


main()