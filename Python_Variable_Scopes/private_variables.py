def isAutomorphic(num):

    if num <= 3:
        return -1

    sq = num * num

    while num > 0:
        if num % 10 != sq % 10:
            return False
        num = num // 10
        sq = sq // 10
    return True


res = isAutomorphic(6)
print("is 6 automorphic", res)

res = isAutomorphic(5)
print("is 5 automorphic", res)


n = int(input("Enter any number"))
x = n ** 2
a = str(n)
b = str(x)
y = len(a)
z = len(b)

print(f"Length of the given number is: ", y)
print(f"Length of the square of the given number is: ", z)
print(f"Result of b.find(a) is: ", b.find(a))


if z - b.find(a) == y:
    print("Automorphic")
else:
    print("Not automorphic number")
