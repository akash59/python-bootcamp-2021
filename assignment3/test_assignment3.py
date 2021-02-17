"""
There is a .zip file called 'unzip_me_for_instructions.zip', unzip it, open the .txt file with Python,
read the instructions and see if you can figure out what you need to do!
"""

import shutil
import os
import re

shutil.unpack_archive('..\\unzip_me_for_instructions.zip', '..\\extracted_instructions', 'zip')
print(os.getcwd())

os.chdir(os.pardir)
current_dir = os.getcwd()

base_path = os.path.join(current_dir, 'extracted_instructions\\extracted_content')
instructions_file_path = os.path.join(base_path, 'Instructions.txt')

with open(instructions_file_path, 'r') as file:
    file_contents = file.read()

print(file_contents)

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

for folder, sub_folders, files in os.walk(base_path):
    print(f'Currently looking at : {folder} \n')
    print('Its sub folders are - \n')
    for sub_folder in sub_folders:
        print(f'Sub folder: {sub_folder} \n')

    print('The files present are - \n')
    for file in files:
        print(f'the file is {file} \n')
        print(os.getcwd())
        file_path = os.path.join(folder, file)
        with open(file_path, 'r') as f:
            f_contents = f.read()
            results = re.search(pattern, f_contents)
            if results is not None:
                break

    if results is not None:
        print(f'Phone number matched is {results.group()}')
        break
