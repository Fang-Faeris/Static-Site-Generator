./main.sh
print("hello world")
from textnode import TextNode, TextType

def main():
    text = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(text)


main()