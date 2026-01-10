from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node has no value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props = self.props_to_html()
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode({None if self.tag == None else self.tag}, {None if self.value == None else self.value}, {None if self.props == None else self.props})"