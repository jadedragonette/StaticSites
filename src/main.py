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
#   gotta figure this out still, brain still overwork-exhausted. Yay me
#   With all luck, I'll be up to properly working on this again in a few days - in the meantime, another cheatery comment update. Blahblahblahblahblahblah. last one. I lied but tomorrow's another day. Perhaps, anyways. Will 100% do stuff tomorrow. just in case because I need sleep
    split = old_nodes.split(delimiter)
    return

def main():
    Test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(Test.__repr__())


main()