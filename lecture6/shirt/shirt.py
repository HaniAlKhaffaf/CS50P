from PIL import Image, ImageOps
import sys

def main():
    valid_extensions = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        sys.exit("missing command-line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not sys.argv[1].lower().endswith(valid_extensions):
        sys.exit("argv[1] is not a valid image file (.jpg, .jpeg, .png)")
    elif not sys.argv[2].lower().endswith(valid_extensions):
        sys.exit("argv[2] is not a valid image file (.jpg, .jpeg, .png)")

    input_extension = sys.argv[1].split('.')[-1].lower()
    output_extension = sys.argv[2].split('.')[-1].lower()
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    photo_shirt(input_file_name, output_file_name)

def photo_shirt(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            result = ImageOps.fit(input, shirt.size)
            result.paste(shirt, mask = shirt)
            result.save(output)
    except FileNotFoundError:
        sys.exit("the file is not found")

if __name__ == "__main__":
    main()