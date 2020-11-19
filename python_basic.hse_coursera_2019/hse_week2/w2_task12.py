# week 2 task 12
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (y2 - y1) % 2 == (x2 - x1) % 2 and (y2 - x2) >= 0:
    if (y2 >= y1) and (x2 >= x1) and (y2 - y1) >= (x2 - x1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
