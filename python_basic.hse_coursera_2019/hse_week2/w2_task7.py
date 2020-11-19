# w2_task7
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
color1 = (x1 % 2 == 0 and y1 % 2 != 0) or (x1 % 2 != 0 and y1 % 2 == 0)
color2 = (x2 % 2 != 0 and y2 % 2 == 0) or (x2 % 2 == 0 and y2 % 2 != 0)
if color1 == color2:
    print("YES")
else:
    print("NO")
