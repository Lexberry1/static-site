from textnode import TextNode, TextType
from copystatic import copy_static
from gencontent import generate_page, generate_pages_recursive
import os
import shutil
source = './static'
destination = './public'

def main():
    print("Deleting public directory...")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    print("Creating public directory...")
    os.mkdir(destination)

    print("Copying static files to public directory...")
    copy_static(source, destination)

    print("Generating page...")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ =="__main__":
    main()
