# week 1 task 24
A = int(input())
B = int(input())
print((0**(A % B) * "YES") + ((1 - (0**(A % B))) * "NO"))
