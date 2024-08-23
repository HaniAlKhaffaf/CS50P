def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print(result)


def shorten(word):
    my_word = ""
    switch = False
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                switch = True
        if switch == False:
            my_word = my_word + letter
        switch = False
    return my_word

if __name__ == "__main__":
    main()  