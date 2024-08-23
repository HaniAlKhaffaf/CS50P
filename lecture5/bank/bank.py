def main():
    userGreeting = input("say your greetings please: ").strip().split(" ")[0]
    result = value(userGreeting)
    print(f"${result}")

def value(greeting):
    if greeting == "hello" or greeting == "Hello":
        return 0
    elif greeting[0] == "h" or greeting[0] == "H":
        return 20
    else: 
        return 100

if __name__ == "__main__":
    main()



