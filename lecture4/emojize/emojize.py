import emoji

def main():
    user_emoji = input("Input: ")
    print(emoji.emojize(f"Output: {user_emoji}", language="alias"))

    # if "_" in user_emoji:
    #     print(emoji.emojize(f"Output: {user_emoji}"))
    # else:




main() 
