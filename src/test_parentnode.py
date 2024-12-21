import unittest

from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", None, None)
#        print(node.to_html())
        node2 = ParentNode("a", None, {"href": "test.site"})
#        print(node2.props_to_html())
#        print(node2.to_html())
        node3 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),],)
        print(node3.children)
        print(node3.children[0])
        print(len(node3.children))
        print(node3.to_html())

if __name__ == "__main__":
    unittest.main()