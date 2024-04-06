import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
key_words = ["-f", "--font"]

len = len(sys.argv)
if len == 1:
    figlet.setFont(font=random.choice(fonts))
elif len == 3:
    if (sys.argv[1] not in key_words) or (sys.argv[2] not in fonts):
        sys.exit("Invalid usage")
    else:
        figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

msg = input("Input: ")
print("Output: ")
print(figlet.renderText(msg))
