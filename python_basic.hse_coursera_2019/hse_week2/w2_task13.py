# w2_task13
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
if c >= a + b:
    print("impossible")
elif c**2 == a**2 + b**2:
    print("rectangular")
elif c**2 < a**2 + b**2:
    print("acute")
elif c**2 > a**2 + b**2:
    print("obtuse")
