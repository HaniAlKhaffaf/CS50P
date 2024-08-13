def main():
    userInput = int(input("Enter a mass so we can find the joules of that mass: "))
    userJoules = calculateInput(userInput)
    print(userJoules)


def calculateInput(x):
    calculatedValue = x * (300000000 * 300000000)
    return calculatedValue  


main()