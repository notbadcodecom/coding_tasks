# Сумма ряда
i = 0
n = float(input())
sum_n = 0
while i < n:
    i += 1
    sum_n += (1 / (i ** 2))
print(sum_n)
