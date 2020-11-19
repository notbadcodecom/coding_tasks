# w2_task15
a, b, c = int(input()), int(input()), int(input())
# if a <= b <= c:
#     print(a, b, c)
# elif a <= c <= b:
#     print(a, c, b)
# elif b <= a <= c:
#     print(b, a, c)
# elif b <= c <= a:
#     print(b, c, a)
# elif c <= a <= b:
#     print(c, a, b)
# else:
#     print(c, b, a)
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
print(a, b, c)
