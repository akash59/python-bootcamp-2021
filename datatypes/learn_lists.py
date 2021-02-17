my_list = [1, 2, 3, 4]
my_new_list = [1, 'aka', (1, 2), 5.6]
print(len(my_list))
print(len(my_new_list))

# slicing and indexing in Lists works just like Strings
print(my_new_list[2])
print(my_new_list[1:])

# list concatenation
concatenated_list = my_list + my_new_list
print(concatenated_list)

# Lists are mutable
my_new_list[1] = 'akash'
print(my_new_list)

# adding to a list
my_new_list.append('newly_appended')
print(my_new_list)

my_new_list.append('newly_appended_again')
print(my_new_list)

# removing from a list
print(concatenated_list)
popped_item = concatenated_list.pop()
print(popped_item)

popped_item_at_specific_index = concatenated_list.pop(2)
print(popped_item_at_specific_index)

# pop with negative index
print(concatenated_list)
neg_popped_item = concatenated_list.pop(-2)
print(neg_popped_item)
print(type(neg_popped_item))

# based on ascii values - https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
letters_list = ['a', 'x', 'd', 'g', 'P', '#', '$']
nums_list = [1, 9, 6, 4, 6]

letters_list.sort()
nums_list.sort()
print(letters_list)
print(nums_list)

nums_list.reverse()
print(nums_list)

l = [1, 1, [1, 2]]
print(l[2][1])
