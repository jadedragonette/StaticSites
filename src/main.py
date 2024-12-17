from textnode import *

def main():
    Test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(Test.__repr__())


main()