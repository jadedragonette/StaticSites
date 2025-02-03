from htmlnode import *
from textnode import *
import re

def text_node_to_html_node(text_node):
    if text_node.TextType == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.TextType == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.TextType == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.TextType == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.TextType == TextType.LINK:
        return LeafNode("a", text_node.text, {href:text_node.url})
    if text_node.TextType == TextType.IMAGE:
        return LeafNode("img", "", {src:text_node.url, alt:text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final = []
    for item in old_nodes:
        if item.text_type != TextType.TEXT or delimiter == "":
            final.append(item)
            continue
        split_nodes = []
        sections = item.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for x in range(len(sections)):
            if sections[x] == "":
                continue
            if x % 2 == 0:
                split_nodes.append(TextNode(sections[x], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[x], text_type))
        final.extend(split_nodes)
    return final

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    for node in old_nodes:
        new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    final = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            final.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raiseValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                final.append(TextNode(sections[0], TextType.TEXT))
            final.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            final.append(TextNode(original_text, TextType.TEXT))
    return final

def text_to_textnodes(text):
        return split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD), "*", TextType.ITALIC), '`', TextType.CODE)))

def markdown_to_blocks(markdown):
    final = []
    cleaning = markdown.split("\n\n")
    for line in cleaning:
        if line == "":
            continue
        line = line.strip()
        final.append(line)
    return final

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith("> "):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph

def text_to_children(text):
    new_nodes = []
    middle_nodes = []
    clean = text.split("\n")
    for line in clean:
        middle_nodes.append(text_to_textnodes(line))
    for node in middle_nodes:
        new_nodes.append(text_node_to_html_node(node))
    return new_nodes

def markdown_to_html_node(markdown):
    step_one = markdown_to_blocks(markdown)
    final = []
    for item in step_one:
        test = block_to_block_type(item)
        if test == "block_type_heading":
#           gonna be here a while, might as well get comfortable...quick addition for the streak, and once again
            if item.startswith("# "):
                tag = h1
            if item.startswith("## "):
                tag = h2
            if item.startswith("### "):
                tag = h3
            if item.startswith("#### "):
                tag = h4
            if item.startswith("##### "):
                tag = h5
            if item.startswith("###### "):
                tag = h6
            clean = item.lstrip("#")
            final.append(HTMLNode(tag, None, text_to_children(clean), None))
                
        if test == "block_type_code":
            HTMLNode(code, item, )
        if test == "block_type_quote":
            HTMLNode (item, )
        if test == "block_type_ulist":
            HTMLNode(item, )
        if test == "block_type_olist":
            HTMLNode(item, )
        if test == "block_type_paragraph":
            HTMLNode(p, item, )