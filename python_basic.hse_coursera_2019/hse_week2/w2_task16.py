# w2_task16
a, b, c = int(input()), int(input()), int(input())
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
if a == b == c:
    print(3)
elif a == b or b == c:
    print(2)
else:
    print(0)
