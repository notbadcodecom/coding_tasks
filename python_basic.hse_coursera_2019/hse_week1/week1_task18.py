# week 1 task 18
seconds = int(input())
h = (seconds // 3600 % 24)
m1 = (seconds // 60 % 60) // 10
m2 = (seconds // 60 % 60) % 10
s1 = (seconds % 60) // 10
s2 = (seconds % 60) % 10
print(h, ":", m1, m2, ":", s1, s2, sep="")
