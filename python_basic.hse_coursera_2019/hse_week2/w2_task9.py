# w2_task9
n = int(input())
if 20 > n > 10 or n % 10 == 0 or 10 > n % 10 > 4:
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
