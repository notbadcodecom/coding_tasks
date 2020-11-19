# week 1 task 22
num = int(input())
one = num // 1000
two = num // 100 % 10
three = num // 10 % 10
four = num % 10
print(0**((one - four)**2 + (two - three)**2))
