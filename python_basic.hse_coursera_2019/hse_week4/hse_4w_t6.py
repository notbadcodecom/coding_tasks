# Возведение в степень
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)
a, n = float(input()), int(input())
print(power(a, n))
