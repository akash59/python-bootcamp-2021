# Unordered learn_collections of unique elements
my_set = set()
my_set.add(1)
print(my_set)

my_set.add(2)
my_set.add(2)
print(my_set)

my_list = [1, 1, 2, 3, 2, 1, 3]
my_new_set = set(my_list)
print(my_new_set)

my_str = 'Mississippi'
print(type(set(my_str)))
print(set(my_str))