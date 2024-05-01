import re


def parse(html):
    if matches := re.search(r'(<iframe(?: width="[0-9]+")?(?: height="[0-9]+")? src="https?://(?:www\.)?youtube.com/embed/\w+"(?: title="(?:\w| )+")?(?: frameborder="\d+")?(?: allow="(\w|-|;| )+")?(?: allowfullscreen)?></iframe>)', html):
        tmp = matches.group(1)
        if msg := re.search(r"(https?://(?:www\.)?youtube.com/embed/\w+)", tmp):
            return re.sub(r"https?://(?:www\.)?youtube.com/embed/", "https://youtu.be/", msg.group(1))
        else:
            return None
    else:
        return None


def main():
    html = input("HTML: ")
    print(parse(html))


if __name__ == "__main__":
    main()
