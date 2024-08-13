def main():
    userGreeting = input("say your greetings please: ").strip().split(" ")[0]
    if userGreeting == "hello" or userGreeting == "Hello":
        print("$0")
    elif userGreeting[0] == "h" or userGreeting[0] == "H":
        print("$20")
    else: 
        print("$100")


main()