def main():
    fruit = {}
    while True:
        try:
            user_input = input().upper()
            if user_input in fruit:
                fruit[user_input] += 1
            else:
                fruit[user_input] = 1
        except EOFError:
            sorted(fruit)
            for _ in fruit:
                print(_, fruit[_])


main()
