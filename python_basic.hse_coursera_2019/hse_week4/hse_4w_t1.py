# Минимум 4 чисел
#def min4(a, b, c, d):
#    if a > b:
#        a = b
#    if c > d:
#        c = d
#    if a <= c:
#        return a
#    return c


def min2(x, y):
    if x < y:
        return x
    return y

a, b = int(input()), int(input())
c, d = int(input()), int(input())
print(min2(min2(a, b), min2(c, d)))
# print(min4(a, b, c, d))
