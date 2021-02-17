from functools import wraps


# few closures examples
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)

    return inner_function


my_func = outer_function()
my_func()
my_func()
my_func()


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func()


def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function


hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func()

"""A decorator is a function that takes in another function as an argument, adds some functionality to it and
returns another function. It does affect the code of the passed in function"""


def decorated_function(my_original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapped executed this before {}'.format(
            my_original_function.__name__))
        return my_original_function(*args, **kwargs)

    return wrapper_function


def display():
    print('display function ran')


# one way of using decorators
decorator_display = decorated_function(display)
decorator_display()


# Another common way of using decorators is by annotations


@decorated_function
def display():
    print('display function ran')


@decorated_function
def display_info(name, age):
    print('my name is {} and age is {}'.format(name, age))


# one way of using decorators
display()

display_info('akash', 30)


def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"

    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


@makebold
@makeitalic
def log(s):
    return s


print(hello())  # returns "<b><i>hello world</i></b>"
print(hello.__name__)  # with functools.wraps() this returns "hello"
print(log('hello'))  # returns "<b><i>hello</i></b>"


def add_logging(orig_func):
    def wrapper(*args, **kwargs):
        print('Executing function -- {} '.format(orig_func.__name__))
        return orig_func(*args, **kwargs)

    return wrapper


@add_logging
def greet(name):
    print('Hello, {}'.format(name))


greet('Akash')
