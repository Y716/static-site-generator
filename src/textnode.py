from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textNode):
        if (self.text == textNode.text 
            and self.text_type == textNode.text_type 
            and self.url == textNode.url):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text.upper()}, {self.text_type.value.upper()}, {None if self.url == None else self.url.upper()})"