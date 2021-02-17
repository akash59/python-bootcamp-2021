import os

PATH = 'C:\\Users\\akash.sood\\Documents\\Work\\Realize\\gitprojects\\python-learning'

print(os.getcwd())

print(os.listdir(PATH))

for folder, sub_folders, files in os.walk(PATH):
    print(f'Currently looking at : {folder} \n')
    print('Its sub folders are - \n')
    for sub_folder in sub_folders:
        print(f'Sub folder: {sub_folder} \n')

    print('The files present are - \n')
    for file in files:
        print(f'the file is {file} \n')