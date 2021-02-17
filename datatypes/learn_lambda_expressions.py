def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Akash', 'Itika', 'Sunidhi', 'Sally', 'Brownie']
print(list(map(splicer, names)))
# help(map)

# filter function
ages = [5, 12, 17, 18, 24, 32]


def my_func(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(my_func, ages)
for x in adults:
    print(x)


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_nums)))

names = ['Akash', 'Itika', 'Sunidhi', 'Sally', 'Brownie']


def check_length(name):
    return len(name) >= 6


for name in filter(check_length, names):
    print(name)

# lambda expression

# def square(num): return num ** 2
square = lambda num: num ** 2

print(list(map(lambda num: num * 2, names)))
print(square(2))

print(list(filter(lambda name: len(name) >= 6, names)))

names = ['Akash', 'Itika', 'Sunidhi', 'Sally', 'Brownie']
print(list(map(lambda ch: ch[0], names)))

names = ['Akash', 'Itika', 'Sunidhi', 'Sally', 'Brownie']
print(list(map(lambda name: name[::-1], names)))