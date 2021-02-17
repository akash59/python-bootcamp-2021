x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# Python follows L.E.G.B. rule

my_name = 'THIS IS A GLOBAL STRING'


def greet():
    my_name = 'Sammy'

    def hello():
        my_name = 'Python'
        print(f'Hello {my_name}')

    hello()


greet()
print(my_name)

my_name = 'GLOBAL VALUE'


def greet():
    global my_name
    print('original global name ' + my_name)
    my_name = 'Python'
    print(f'Hello {my_name}')


greet()
print(my_name)
