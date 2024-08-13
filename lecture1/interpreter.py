def main():
    userInput = input("This is a simple maths interpreter, write the formula you want to calculate: ")
    firstNum = float(userInput.split(" ")[0])
    operation = userInput.split(" ")[1]
    secondNum = float(userInput.split(" ")[2])

    match operation:
        case "+":
            print(round(firstNum + secondNum, 1))
        case "-":
            print(round(firstNum - secondNum, 1))
        case "*":
            print(round(firstNum * secondNum, 1))
        case "/":
            if secondNum != 0:
                print(round(firstNum / secondNum, 1))
            else:
                print("you cannot divide anything by zero")


main()