my_file = open('test.txt')
# print(my_file.read())
my_file.seek(0)
contents = my_file.read()
# print(contents)
my_file.seek(0)

lines = my_file.readlines()
print(lines)
my_file.close()

#  for windows use \\ in file path
#  for linux use /

#  use context manager for file io operations - no need to explicit close file connections
with open('test.txt') as my_new_file:
    my_contents = my_new_file.read()
    print(my_contents)

with open('test.txt', mode='r') as ff:
    print(ff.read())

with open('test.txt', mode='a') as ff:
    ff.write('\nFOUR ON FOURTH')

with open('test.txt', mode='r') as ff:
    print(ff.read())

with open('newly_written_file.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')

with open('newly_written_file.txt', mode='r') as ff:
    print(ff.read())

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/00-Python%20Object%20and%20Data%20Structure%20Basics/08-Files.ipynb

# Passing 'w+' lets us read and write to the file
"""
Opening a file with 'w' or 'w+' truncates the original, 
meaning that anything that was in the original file is deleted!
"""
with open('newly_written_file.txt', mode='w+') as f:
    f.write('I CREATED THIS FILE AGAIN!')
    f.seek(0)
    print(f.read())

"""
Like 'w+', 'a+' lets us read and write to a file. 
If the file does not exist, one will be created.
"""
with open('newly_written_file.txt', mode='a+') as f:
    f.write('\nOPENED THIS FILE FOR APPENDING!')
    f.seek(0)
    print(f.read())

"""
Iterating through a File
"""
for line in open('test.txt'):
    print(line)
