import random


def main():
    user_level = get_level()
    score = 0 
    for _ in range(10):
        counter = 0
        x, y = generate_integer(user_level)
        while True:
            try:
                user_sol = int(input(f"{x} + {y} = "))
                if user_sol == x + y:
                    counter = 0
                    score = score + 1
                    break
                else:
                    counter = counter + 1
                    print("EEE")
                    if counter == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            user_level = int(input("Level: "))
            if user_level < 1 or user_level > 3:
                raise ValueError
            return user_level
        except ValueError:
            print("Invalid level! Please enter a level between 1 and 3.")


def generate_integer(level):
    if level == 1:
        level = 9
    elif level == 2:
        level = 99 
    else: 
        level = 999

    x = random.randint(1, level)
    y = random.randint(1, level)
    return x, y 



# def generate_integer(level):
#     if level == 1:
#         level = 9
#     elif level == 2:
#         level = 99 
#     else: 
#         level = 999

#     score = 0 
#     for _ in range(10):
#         x = random.randint(1, level)
#         y = random.randint(1, level)
#         counter = 0
#         while True:
#             try:
#                 user_sol = int(input(f"{x} + {y} = "))
#                 if user_sol == x + y:
#                     counter = 0
#                     score = score + 1
#                     break
#                 else:
#                     counter = counter + 1
#                     print("EEE")
#                     if counter == 3:
#                         print(f"{x} + {y} = {x + y}")
#                         break
#             except ValueError:
#                 print("EEE")
#     print(f"Score: {score}")



if __name__ == "__main__":
    main() 