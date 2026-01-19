import re
from textnode import TextType, TextNode
from leafnode import LeafNode

def text_node_to_html_node(textnode) -> LeafNode:
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
    
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text_lists = old_node.text.split(delimiter)

        if len(text_lists)%2 == 0:
            raise Exception("Invalid Markdown Syntax")
        for i, piece in enumerate(text_lists):
            if piece == "":
                continue
            if i%2==0:
                new_nodes.append(TextNode(piece, TextType.TEXT))
            else:
                new_nodes.append(TextNode(piece, text_type))

    return new_nodes
        
def extract_markdown_images(text) -> list[tuple]:
    alt_images = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return alt_images

def extract_markdown_links(text) -> list[tuple]:
    alt_links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return alt_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text_lists = re.split(r'\!\[(.*?)\)', old_node.text)
        alt_images = extract_markdown_images(old_node.text)
        
        if len(text_lists)%2 == 0:
            raise Exception("Invalid Markdown Syntax")
        for i, piece in enumerate(text_lists):
            if piece == "":
                continue
            if i%2==0:
                new_nodes.append(TextNode(piece, TextType.TEXT))
            else:
                alt_image = alt_images[0]
                alt_images.remove(alt_image)
                new_nodes.append(TextNode(text=alt_image[0], text_type=TextType.IMAGE, url=alt_image[1]))

    return new_nodes

def split_nodes_link(old_nodes) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text_lists = re.split(r'\[(.*?)\)', old_node.text)
        alt_links = extract_markdown_links(old_node.text)
        
        if len(text_lists)%2 == 0:
            raise Exception("Invalid Markdown Syntax")
        for i, piece in enumerate(text_lists):
            if piece == "":
                continue
            if i%2==0:
                new_nodes.append(TextNode(piece, TextType.TEXT))
            else:
                alt_link = alt_links[0]
                alt_links.remove(alt_link)
                new_nodes.append(TextNode(text=alt_link[0], text_type=TextType.LINK, url=alt_link[1]))

    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    new_nodes = []
    old_node = TextNode(text=text, text_type=TextType.TEXT)
    new_nodes = split_nodes_delimiter([old_node], delimiter="**", text_type=TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, delimiter="`", text_type=TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, delimiter="_", text_type=TextType.ITALIC)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes


