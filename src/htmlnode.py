class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""

        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({None if self.tag == None else self.tag}, {None if self.value == None else self.value}, {None if self.children == None else self.children}, {None if self.props == None else self.props})"
        
    