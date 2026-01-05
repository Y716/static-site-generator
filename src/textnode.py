from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
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