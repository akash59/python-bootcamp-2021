# Write program to check if a given number is Automorphic or not.


# What is an Automorphic number?

# If the given number is present at the end of its square, it is called Automorphic.

# E.g.

# Number: 25    Square: 625

# Number 6        Square: 36

# 25 and 6 are automorphic numbers


# Number: 15    Square: 225

# 15 is Not Automorphic


# Return 1 if the given number if Automorphic

# Return -1 if the given number is not Automorphic


# Write code considering optimisation as well as error handling


def isAutomorphic(number):
    # taking the square of the number
    square = number * number

    # comparing the digits of the given number with the square
    while number > 0:
        if(number % 10 != square % 10):
            # pattern doesn't match, returing -1
            return -1
        # moving to the next digit
        number = number / 10
        square = square / 10
    # number is automorphic, returing 1
    return 1


if isAutomorphic(5) > 0:
    print("Number 5 is Automorphic")
else:
    print("Number 5 is not Automorphic")

if isAutomorphic(6) > 0:
    print("Number 6 is Automorphic")
else:
    print("Number 6 is not Automorphic")


def isAutomorphic()
#  z is length of square of the given number
#  b is string representation of square of the given number
#  y is length of string representation of the given number
    if(z - b.find(a) == y):
        return 1

# abc.log
# Make Model Quantity
# Dell Latitude 25
# HP Pavilion 26
# IBM Balde 45
# HP Envy 18

# cat path/to/file/abc.log | grep "HP Pavilion"
# # HP Pavilion 26

