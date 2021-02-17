def makes_twenty(n1, n2):
    if (n1 + n2) == 20:
        return True
    elif n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(2, 3))
print(makes_twenty(20, 10))


def master_yoda(text):
    words = text.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return " ".join(reversed_words)


out1 = master_yoda("I am home")
out2 = master_yoda("We are Ready")
print(out1)
print(out2)


def summer_69(arr):
    my_sum = 0
    is_add = True

    for num in arr:
        while is_add:
            if num != 6:
                my_sum += num
                break
            else:
                is_add = False
        while not is_add:
            if num != 9:
                break
            else:
                is_add = True
                break
    return my_sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


def count_primes(num):
    prime = 0
    for n in range(2, num + 1):
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                break
        else:
            prime += 1
    return prime


print(count_primes(100))

filename = __file__
# pdb.set_trace()
print(f'filename is {filename}')
count_primes(100)

# for else in python - in this case - else block only executes if for loop fully executes.
for i in range(1, 4):
    break
else:  # Executed because no break in for
    print("No Break")

import string


def is_pangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ", "")
    str1 = set(str1.lower())
    other_str = set(alphabet)
    return str1 == other_str


print(is_pangram("The quick brown fox jumps over the lazy dog"))

print('OXX'[::-1] == 'XXO')

import random
print(random.randint(1, 2))

num1 = 10_000_000_000
num2 = 10_00_000
total = num1 + num2

print(num1 + num2)


a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)


a, b, *c, d = (1, 2, 3, 4, 5)
print(c)


def display_info(name, age):
    print(f'my name is {name} and age is {age}')