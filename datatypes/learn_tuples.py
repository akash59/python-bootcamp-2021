# Tuples are immutable
t = (1, 2, 3)
print(type(t))

t = (1, 'one', 4.5)
print(len(t))
print(t[-1])

# methods
t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print(t.index('b'))

# TypeError: 'tuple' object does not support item assignment
# t[2] = 'NEW'
# print(t)