import pyfiglet
import sys
import random

def main():


    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            try:
                f = pyfiglet.Figlet(font=sys.argv[2])
                user_input = input("Input: ")
                print(f.renderText(user_input))
            except:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    elif len(sys.argv) == 1:
        available_fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(available_fonts)
        figlet = pyfiglet.Figlet(font=random_font)
        user_input = input("Input: ")
        print(figlet.renderText(user_input))
    else:
        sys.exit("Invalid Usage")

main()