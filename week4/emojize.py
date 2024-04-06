#pip install emoji
#URL:pypi.org/project/emoji
import emoji

msg = input("Input: ")
print(emoji.emojize(f"Output: {msg}", language="alias"))
