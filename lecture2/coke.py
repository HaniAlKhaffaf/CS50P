def main():
    calculations(authentication(50))

def calculations(money):
    price = 0
    due = 50
    while True:
        price = price + money
        due = due - money
        if price == 50:
            print("Change Owed: ", price - 50)
            break
        if price > 50:
            print("Change Owed: ", price - 50)
            break
        money = authentication(due)

def authentication(due):
    print("Amount Due: ", due)
    user_input = int(input("Insert Coin: "))
    while True: 
        if user_input == 5 or user_input == 10 or user_input == 25:
            break
        else:
            print("Amount Due: ", due)
            user_input = int(input("Insert Coin: "))

    return user_input


main()