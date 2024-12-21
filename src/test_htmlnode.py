import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Testing test", None, {"href": "test.com"})
        node2 = HTMLNode("p", "Testing test", None, {"href": "test.com", "target": "blank"})
        print(node.props_to_html())
        print(node2.props_to_html())

if __name__ == "__main__":
    unittest.main()