
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        for item in self.props:
            string += f' {item}="{self.props[item]}"'
        return string
    
    def __repr__(self):
        print(f"tag = {self.tag}; value = {self.value}; children = {self.children}; props = {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children, props):
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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        string = ""
        if self.tag == None:
            raise ValueError("No tag present")
        if self.children == None:
            raise ValueError("No children present")
        def build_the_string(self):
            if self.children == None:
                return string
            string += self.children[0]
            return build_the_string(self.children[1:])
        return