# week 2 task 22
k, m, n = int(input()), int(input()), int(input())
if n % k == 0 and n >= k:
    print(n // k * m * 2)
elif n % k != 0 and n > k:
    print((n // k + 1) * m * 2)
elif n % k != 0 and n < k:
    print(m * 2)
