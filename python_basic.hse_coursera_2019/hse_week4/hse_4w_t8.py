# Быстрое возведение в степень
def QuikExp(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return QuikExp(a * a, n // 2)
    else:
        return a * QuikExp(a, n-1)
a, n = float(input()), int(input())
print(QuikExp(a, n))
