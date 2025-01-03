from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    if text_node.TextType == TEXT:
        LeafNode(None, text_node.text)
    if text_node.TextType == BOLD:
        LeafNode("b", text_node.text)
    if text_node.TextType == ITALIC:
        LeafNode("i", text_node.text)
    if text_node.TextType == CODE:
        LeafNode("code", text_node.text)
    if text_node.TextType == LINK:
        LeafNode("a", text_node.text, , {href:text_node.url})
    if text_node.TextType == IMAGE:
        LeafNode("img", "", , {src:text_node.url, alt:text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split = old_nodes.split(delimiter)
    return

def main():
    Test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(Test.__repr__())


main()