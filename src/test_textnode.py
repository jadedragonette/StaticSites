import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("Testing", TextType.ITALIC, None)
        node4 = TextNode("Testing", TextType.ITALIC, None)
        self.assertEqual(node3, node4)
#        node5 = TextNode("Testing", TextType.NORMAL, "blah")
#        node6 = TextNode("Testing", TextType.CODE, "blah")
#        self.assertEqual(node5, node6)



if __name__ == "__main__":
    unittest.main()