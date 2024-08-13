def main():
    userInput = input()
    convertedInput = convert(userInput)
    print(convertedInput)

def convert(x):
    return x.replace(":)", "\U0001F642").replace(":(", "\U0001F641")

main()