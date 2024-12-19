from htmlnode import *

class LeafNode(HTMLNode):
    def __init(self, tag, value, children, props):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.tag == "p" or self.tag == "b" or self.tag == "i" or self.tag == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.tag == "a":
            return f"<a{self.props_to_html()}>{self.value}</a>"
        if self.tag == "img":
            return f"<img {self.props_to_html()} alt={self.value}>"