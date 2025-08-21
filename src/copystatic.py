import os
import shutil

def copy_static(source, destination):
	if not os.path.exists(source):
		raise Exception("Source directory needed")
	if os.path.exists(destination):
		shutil.rmtree(destination)
	os.mkdir(destination)
	contents = os.listdir(source)
	for content in contents:
		source_path = os.path.join(source, content)
		destination_path = os.path.join(destination, content)
		if os.path.isfile(source_path):
			shutil.copy(source_path, destination_path)
		else:
			os.mkdir(destination_path)
			copy_static(source_path, destination_path)

