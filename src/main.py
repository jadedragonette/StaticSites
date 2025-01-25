from htmlnode import *
from textnode import *
from split_nodes_delimiter import *


def main():
    Test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(Test.__repr__())


main()