"""
Learning Generators
"""


def create_cubes(n):
    return [x ** 3 for x in range(0, n + 1)]


cubes = create_cubes(10)
print(cubes)

# Redefine the same function again using generator
"""
Generators are much more memory efficient
"""


def create_cubes(n):
    for x in range(0, n + 1):
        yield x ** 3


# either
print(list(create_cubes(10)))

# or
cubes = create_cubes(10)
print(cubes)
for cube in cubes:
    print(cube)

s = 'hello'
iter_s = iter(s)
print(type(iter_s))
print(next(iter_s))

# generator comprehension!
my_list = [1, 2, 3, 4, 5]

gen_comp = (item for item in my_list if item > 3)
print(gen_comp)

for item in gen_comp:
    print(item)