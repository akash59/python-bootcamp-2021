my_list = [1, 2, 4]
my_list_1 = ['a', 'b', 'c']
zipped_list = zip(my_list, my_list_1)
# print(zipped_list)
# print(list(zipped_list))

# for item in zipped_list:
#     print(item)

for v1, v2 in zipped_list:
    print(v1)
    print(v2)

word = 'akash'
for index, letter in enumerate(word):
    print(f'At index {index} letter is {letter}')

for item in enumerate(word):
    print(item)

# other operators
#  min, max, in

#  random module
from random import shuffle, randint

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(my_list)
print(my_list)

my_num = randint(1, 100)
print(my_num)