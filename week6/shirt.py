from PIL import Image, ImageOps
import sys
import os.path



def check_filename():
    exts = [".jpg", ".jpeg", ".png"]
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    else:
        if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
            sys.exit("Files have different extension")
        else:
            return (os.path.splitext(sys.argv[1])[1].lower() in exts) and (os.path.splitext(sys.argv[2])[1].lower() in exts)


def convert():
        try:
            shirt = Image.open("shirt.png")
            image_input = ImageOps.fit(Image.open(sys.argv[1]), shirt.size)
        except FileNotFoundError:
            sys.exit("File does not exit")
        else:
            image_input.paste(shirt, box=(image_input.size[0] - shirt.size[0], image_input.size[1] - shirt.size[1]), mask=shirt)
            image_input.save(sys.argv[2])


def main():
    if check_filename():
        convert()
    else:
        sys.exit("Invalid FileType")


if __name__ == "__main__":
    main()
