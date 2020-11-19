# Проверка числа на простоту
def IsPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return "NO"
        i += 1
    return "YES"
n = int(input())
print(IsPrime(n))
