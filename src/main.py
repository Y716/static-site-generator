import os
import shutil
import sys
from gen_content import copy_content, generate_page_recursive

dir_path_public = "./docs/"
dir_path_static = "./static/"
dir_path_template = "template.html"
dir_path_from = "./content"

def main():
    basepath = sys.argv[0]
    if len(sys.argv) <= 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")
    copy_content(dir_path_static, dir_path_public)
    generate_page_recursive(
        dir_path_from, 
        dir_path_template,
        dir_path_public,
        basepath)
    
    

if __name__ == "__main__":
    main()