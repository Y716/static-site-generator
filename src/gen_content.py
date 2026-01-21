import os
import shutil
from blocks_markdown import markdown_to_html_node


def copy_content(source, destination):
    print(f"Making {destination} directory...")
    os.mkdir(destination)
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)
        if os.path.isfile(source_path):
            shutil.copy(src=source_path, dst=destination)
            print(f"Add '{filename}' to {destination_path}")
        else:
            destination_path += "/"
            copy_content(source_path, destination_path)

def extract_title(markdown: str) -> str:
    lines = markdown.split(sep="\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            line = line.replace("# ", "")
            return line

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating Pages from {from_path} to {dest_path} using {template_path}")
    with open(from_path, mode='r') as file:
         content = file.read()
    with open(template_path, mode='r') as file:
         template = file.read()
    html_nodes = markdown_to_html_node(content)
    html_page = html_nodes.to_html()
    title = extract_title(content)
    full_html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_page)
    
    with open(dest_path, mode="w") as dest_file:
        dest_file.write(full_html_page)

def generate_page_recursive(dir_path_content: str, template_path: str, dir_path_dest: str):
    for filename in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, filename)
        destination_path = os.path.join(dir_path_dest, filename)
        if os.path.isfile(content_path):
            destination_path = destination_path.replace(".md", ".html")
            generate_page(content_path, template_path, destination_path)
        else:
            destination_path += "/"
            os.mkdir(destination_path)
            generate_page_recursive(content_path, template_path, destination_path)
    
    
    
    
            
