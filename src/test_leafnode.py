import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "all the test")
        print(node.to_html())
        node2 = LeafNode("a", "testing, testing", None, {"href": "test.site"})
        print(node2.props_to_html())
        print(node2.to_html())