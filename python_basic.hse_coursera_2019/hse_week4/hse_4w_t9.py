# Сократите дробь
def ReduceFraction(n, m):
    def CommonDivisor(n, m):
        if m == 0:
            return n
        elif n > m:
            m, n = n, m
        return CommonDivisor(n, m % n)
    nod = CommonDivisor(n, m)
    return n // nod, m // nod
n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
