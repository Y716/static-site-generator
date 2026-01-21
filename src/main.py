import os
import shutil
from gen_content import copy_content, generate_page_recursive

dir_path_public = "./public/"
dir_path_static = "./static/"
dir_path_template = "template.html"
dir_path_from = "./content"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")
    copy_content(dir_path_static, dir_path_public)
    generate_page_recursive(
        dir_path_from, 
        dir_path_template,
        dir_path_public)
    
    

if __name__ == "__main__":
    main()