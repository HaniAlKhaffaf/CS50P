def main():
    names = get_user_inputs()
    farewell_message = adieu(names)
    print(farewell_message)


def adieu(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell_message = "Adieu, adieu, to "
        for i in range(len(names) - 1):
            farewell_message += names[i]
            if i < len(names) - 2:
                farewell_message += ", "
            else:
                farewell_message += ", and "
        farewell_message += names[-1]
        return farewell_message

def get_user_inputs():
    inputs = []
 
    while True:
        try:
            line = input("Name: ")
            inputs.append(line)
        except EOFError:
            break

    return inputs


if __name__ == "__main__":
    main()
