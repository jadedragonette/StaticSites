import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "all the test")
        print(node.to_html())
        node2 = LeafNode("a", "testing, testing", {"href": "test.site"})
        print(node2.props_to_html())
        print(node2.to_html())

if __name__ == "__main__":
    unittest.main()