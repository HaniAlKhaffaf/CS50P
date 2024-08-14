import random
import sys

def main():
    r = random.Random()
    user_number = get_int()
    random_number = r.randint(1, user_number)
    guess(random_number)


def guess(random_number):
    try:
        user_guess = int(input("Guess: "))
        if user_guess < 1:
            guess(random_number)
        if user_guess > random_number:
            print("Too large!")
            guess(random_number)
        elif user_guess < random_number:
            print("Too small!")
            guess(random_number)
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        guess(random_number)
        



def get_int():
    try:
        user_input = int(input("Level: "))
        if user_input < 1:
            get_int()
        return user_input
    except ValueError:
        print("Enter an Integer")
        get_int()




main()