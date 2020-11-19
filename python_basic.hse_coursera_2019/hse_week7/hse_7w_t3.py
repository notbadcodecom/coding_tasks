#  Встречалось ли число раньше
digits = list(map(int, input().split()))
tmp = set()
for digit in digits:
    if digit in tmp:
        print('YES')
    else:
        print('NO')
        tmp.add(digit)
