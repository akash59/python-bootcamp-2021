"""
There is a .zip file called 'unzip_me_for_instructions.zip', unzip it, open the .txt file with Python,
read the instructions and see if you can figure out what you need to do!
"""

import shutil
import os
import re


PATTERN = re.compile(r'(\d{3})-(\d{3})-(\d{4})')


def read_instructions_file(filename):
    os.chdir(os.pardir)
    current_dir = os.getcwd()
    global BASE_PATH
    BASE_PATH = os.path.join(current_dir, 'extracted_instructions\\extracted_content')
    instructions_file_path = os.path.join(BASE_PATH, filename)
    with open(instructions_file_path, 'r') as instructions_file:
        file_contents = instructions_file.read()
    print(file_contents)


def search_pattern_in_a_file(f_path):
    with open(f_path, 'r') as f:
        f_contents = f.read()
        search_results = re.search(PATTERN, f_contents)
        if search_results is not None:
            return search_results
        else:
            pass


def scan_directory_for_patterns():
    scanned_results = []
    actual_file_name = ''
    for folder, sub_folders, files in os.walk(BASE_PATH):
        for file in files:
            file_path = os.path.join(folder, file)
            res = search_pattern_in_a_file(file_path)
            scanned_results.append(res)
            if res is not None:
                actual_file_name = file_path

    return scanned_results, actual_file_name


class Assignment3:

    def __init__(self, zipped_file_path, file_extn):
        self.zipped_file_path = zipped_file_path
        self.file_extn = file_extn

    def unzip_archive(self, extract_location='..\\extracted_instructions'):
        shutil.unpack_archive(self.zipped_file_path, extract_location, self.file_extn)


if __name__ == '__main__':
    assignment3 = Assignment3('..\\unzip_me_for_instructions.zip', 'zip')
    assignment3.unzip_archive()
    read_instructions_file('Instructions.txt')
    results, file_name = scan_directory_for_patterns()
    for result in results:
        if result is not None:
            print(f'{result.group()} is present in file {file_name}')
