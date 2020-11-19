# week 1 task 12
A = int(input())
B = int(input())
N = int(input())
count = (A * 100 + B) * N
count_rub = count // 100
count_kop = count % 100
print(count_rub, count_kop)
