import justsayhello

justsayhello.hello()

print(justsayhello.__file__)
print(justsayhello.__name__)


def isAutomorphic(num):
    sq = num * num
    while num > 0:
        if num % 10 != sq % 10:
            return False
        num = num / 10
        sq = sq / 10
    return True


res = isAutomorphic(6)
print("is 6 automorphic", res)

res = isAutomorphic(5)
print("is 5 automorphic", res)
