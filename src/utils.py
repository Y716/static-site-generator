from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(textnode):
    if textnode.text_type not in TextType:
        raise Exception("Text Type is not valid")
    elif textnode.text_type == TextType.TEXT:
        return LeafNode(value=textnode.text)
    elif textnode.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=textnode.text)
    elif textnode.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=textnode.text)
    elif textnode.text_type == TextType.CODE:
        return LeafNode(tag="code", value=textnode.text)
    elif textnode.text_type == TextType.LINK:
        return LeafNode(tag="a", value=textnode.text, props={"href": textnode.url})
    elif textnode.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": textnode.url, "alt": textnode.text})