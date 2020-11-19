# w2_task17
a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if c <= b:
    (c, b) = (b, c)
    if b <= a:
        (a, b) = (b, a)
        if c <= b:
            (c, b) = (b, c)
elif b <= a:
    (a, b) = (b, a)
    if c <= b:
        (c, b) = (b, c)
if e <= d:
    (e, d) = (d, e)
if a <= d and b <= e:
    print("YES")
elif b <= d and c <= e:
    print("YES")
elif a <= d and c <= e:
    print("YES")
else:
    print("NO")
