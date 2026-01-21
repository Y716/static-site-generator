import re
from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from parentnode import ParentNode
from inline_markdown import text_node_to_html_node, text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if (block.startswith("# ") 
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith("> "):
        lines = block.splitlines()
        for line in lines:
            if not line.startswith("> "):
                if line == ">":
                    continue
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        lines = block.splitlines()
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        lines = block.splitlines()
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    lines = markdown.split(sep="\n")
    blocks = []
    current_block = ""
    for line in lines:
        if line == "" or line.isspace():
            blocks.append(current_block)
            current_block = ""
        else:
            line = line.strip()
            if current_block:
                current_block = current_block+"\n"+line
            else:
                current_block = line
    if current_block:
        blocks.append(current_block)
        current_block = ""
    blocks = [s for s in blocks if s]
    return blocks

def get_tag(blocktype: BlockType, text: str) -> tuple[str, str]:
    match(blocktype):
        case BlockType.PARAGRAPH:
            return "p", text
        case BlockType.HEADING:
            match = re.match(r"^#*", text)
            if len(match.group(0)) == 0:
                raise Exception("Heading error")
            else:
                text = text.replace(f"{match.group(0)} ", "")
                return f"h{len(match.group(0))}", text
        case BlockType.QUOTE:
            text = text.replace("> ", "").replace(">", "\n")
            return "blockquote", text
        case BlockType.CODE:
            text = text.strip("```").lstrip()
            return "pre", text
        case BlockType.UNORDERED_LIST:
            text = text.replace("- ", "")
            return "ul", text
        case BlockType.ORDERED_LIST:
            text = re.sub(r"[0-9]. ", "", text)
            return "ol", text

def text_to_children(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    children_nodes = []
    for node in text_nodes:
        child = text_node_to_html_node(node)
        children_nodes.append(child)
    
    return children_nodes
    
        
def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag, content = get_tag(block_type, block)
        children = []
        if block_type == BlockType.CODE:
            node = TextNode(text=content, text_type=TextType.CODE)
            children = [text_node_to_html_node(node)]
        elif block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            lines = content.split("\n")
            li_nodes = []
            for line in lines:
                if not line.strip():
                    continue
                li_children = text_to_children(line)
                li_nodes.append(ParentNode(tag="li", children=li_children))
            children = li_nodes
        else:
            content = content.replace("\n", " ")
            children = text_to_children(content)
        html_node = ParentNode(tag=tag, children=children)
        html_nodes.append(html_node)
    
    return ParentNode(tag="div", children=html_nodes)