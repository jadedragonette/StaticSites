
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        string = ""
        for item in self.props:
            string += f' {item}="{self.props[item]}"'
        return string
    
    def __repr__(self):
        print(f"tag = {self.tag}; value = {self.value}; children = {self.children}; props = {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        string = ""
        if self.tag == None:
            raise ValueError("No tag present")
        if self.children == None:
            raise ValueError("No children present")
        for item in self.children:
            string += item.to_html()
        return f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"