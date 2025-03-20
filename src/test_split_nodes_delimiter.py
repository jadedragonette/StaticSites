import unittest

from textnode import *
from htmlnode import *
from split_nodes_delimiter import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq(self):
#        first tested the "not Markdown code" Exception, then commented out the test so it would pass again
#        nodeset = TextNode("testing", "text")
#        split_nodes_delimiter([nodeset], "", TextType.NORMAL)
        nodeset1 = TextNode("Testing to see if *stuff* works correctly", TextType.TEXT)
        new_nodes = split_nodes_delimiter([nodeset1], "*", TextType.ITALIC)
        nodeset2 = TextNode("*What* happens if it starts with italic", TextType.TEXT)
        new_nodes2 = split_nodes_delimiter([nodeset2], "*", TextType.ITALIC)
        nodeset3 = TextNode("What happens if it ends with *italic*", TextType.TEXT)
        new_nodes3 = split_nodes_delimiter([nodeset3], "*", TextType.ITALIC)
        nodeset4 = TextNode("Testing the **bold** functionality", TextType.TEXT)
        new_nodes4 = split_nodes_delimiter([nodeset4], "**", TextType.BOLD)
        nodeset5 = TextNode("Testing the 'code' functionality", TextType.TEXT)
        new_nodes5 = split_nodes_delimiter([nodeset5], "'", TextType.CODE)
        nodeset6 = TextNode("Testing for just text", TextType.TEXT)
        new_nodes6 = split_nodes_delimiter([nodeset6], "", TextType.TEXT)

        final = split_nodes_delimiter([nodeset1, nodeset2, nodeset3], "*", TextType.ITALIC)

    def test_text_to_text_node(self):
        text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    
    def test_markdown_to_blocks(self):
        markdown_to_blocks("""# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item
            """)
        md = """
            This is **bolded** paragraph

            This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line

            * This is a list
            * with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
            This is **bolded** paragraph




            This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line

            * This is a list
            * with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
         )

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()