# w2_task26
digit = int(input())
i = digit
min_divisor = 0
while i != 1:
    if digit % i == 0:
        min_divisor = i
        i = i - 1
    else:
        i = i - 1
print(min_divisor)
