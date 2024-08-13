def main():
    switch = False
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    user_input = input("Input: ")
    for letter in user_input:
        for vowel in vowels:
            if letter == vowel:
                switch = True
        if switch == False:
            print(letter, end="")
        switch = False

main()