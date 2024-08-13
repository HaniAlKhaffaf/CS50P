def main():
    fraction = input_verification()
    fraction = fraction * 100
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")

def input_verification():
    while True:
        try:
            user_input = input("Fraction: ").split("/")
            value_x = int(user_input[0])
            value_y = int(user_input[1])
            if value_x > value_y:
                continue
            else:
                return value_x / value_y
        except (ValueError, ZeroDivisionError):
            pass


main()