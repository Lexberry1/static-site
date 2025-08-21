from htmlnode import ParentNode
from markdown_blocks import markdown_to_html_node
import os
def extract_title(markdown):
	lines = markdown.split('\n')
	for line in lines:
		if line.startswith('# '):
			new_line = line[2:]
			final = new_line.strip()
			return final
	raise Exception('No h1 header')

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to{dest_path} using {template_path}")
	with open(from_path, 'r') as markdown_file:
		markdown_contents = markdown_file.read()

	with open(template_path, 'r') as template_file:
		template_contents = template_file.read()

	html_node = markdown_to_html_node(markdown_contents)
	html_string = html_node.to_html()
	title = extract_title(markdown_contents)

	template_contents = template_contents.replace("{{ Title }}", title)
	template_contents = template_contents.replace("{{ Content }}", html_string)

	dest_dir = os.path.dirname(dest_path)
	if dest_dir != "":
		os.makedirs(dest_dir, exist_ok=True)

	with open(dest_path, 'w') as dest_file:
		dest_file.write(template_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	contents = os.listdir(dir_path_content)
	for content in contents:
		full_path = os.path.join(dir_path_content, content)
		if os.path.isfile(full_path):
			if full_path.endswith(".md"):
				dest_file_path = os.path.join(dest_dir_path, content.replace(".md", ".html"))
				generate_page(full_path, template_path, dest_file_path)
		else:
			new_dest_dir = os.path.join(dest_dir_path, content)
			generate_pages_recursive(full_path, template_path, new_dest_dir)
