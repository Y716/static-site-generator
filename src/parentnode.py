from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: No tag")
        if self.children is None:
            raise ValueError("Invalid HTML: No children node")
        html_string = ""

        for child in self.children:
            html_string += child.to_html()
        
        if self.props is not None:
            return f"<{self.tag}>{html_string}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"