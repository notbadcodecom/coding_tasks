# week 1 task 23
A = int(input())
B = int(input())
C = ((A // B + 2) // (A // B + 1)) % 2
D = (C + 1) % 2
print(A * C + B * D)
