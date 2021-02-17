h = 'hello'
s = 'this is also a string'
u = "I'm going on a run"
ui = "I'm going \n on a run"
my_string = 'abcdefghijk'

print(h)
print(s)
print(u)
print(ui)
i = 0
for w in ui:
    print(w, i)
    i = i + 1

print(u[2:])
print(u[:9])

print(my_string[::2])
print(my_string[::3])
print(u[::3])

# print an entire string -
#  first colon means = pick from the start index 0
#  second colon means = end on the last index say n
print(my_string[::])

# reverse a string trick
print(my_string[::-1])

print('Hello World'[8])

# datatypes are immutable
# my_string[0] = 'r'

name = 'Sam'
# form 'PAM' from name var above
last_letters = name[1:]
new_name = 'P' + last_letters
print(new_name)

# concatenation
x = 'Hello World'
print(x + ' it is beautiful outside')

letter = 'z'
print(letter * 10)

x = 'Hello World'
print(x.upper())
print(x)

# splitting a string
x = 'this is a string'
print(x.split())
print(x.split('i'))

# string formatting or interpolation
my_str = 'hello, {} !! Welcome to {}'.format('Akash', 'Druva')
print(my_str)

my_str = 'hello, {0} !! Welcome to {1}'.format('Akash', 'Druva')
print(my_str)

my_str = 'hello, {1} !! Welcome to {0}'.format('Akash', 'Druva')
print(my_str)

# preferred way
my_str = 'hello, {name} !! Welcome to {company}'.format(name='Akash', company='Druva')
print(my_str)

# Float formatting using format method
result = 100/777
print(result)
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))

result = 104.12345
print('The result was {r:1.4f}'.format(r=result))

# F strings - introduced in 3.6 version
name = 'Jose'
age = 10
print(f"Hello, his name is {name} and his age is {age}")
