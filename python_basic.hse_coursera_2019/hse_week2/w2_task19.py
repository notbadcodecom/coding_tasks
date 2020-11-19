# w2_task19
l1, h1, w1 = int(input()), int(input()), int(input())
l2, h2, w2 = int(input()), int(input()), int(input())
x1 = (l1 // l2) * (h1 // h2) * (w1 // w2)
x2 = (l1 // h2) * (h1 // w2) * (w1 // l2)
x3 = (l1 // w2) * (h1 // l2) * (w1 // h2)
x4 = (l1 // l2) * (h1 // w2) * (w1 // h2)
x5 = (l1 // h2) * (h1 // l2) * (w1 // w2)
x6 = (l1 // w2) * (h1 // h2) * (w1 // l2)
if x1 >= x2 and x1 >= x3 and x1 >= x4 and x1 >= x5 and x1 >= x6:
    print(x1)
elif x2 >= x1 and x2 >= x3 and x2 >= x4 and x2 >= x5 and x2 >= x6:
    print(x2)
elif x3 >= x1 and x3 >= x2 and x3 >= x4 and x3 >= x5 and x3 >= x6:
    print(x3)
elif x4 >= x1 and x4 >= x2 and x4 >= x3 and x4 >= x5 and x4 >= x6:
    print(x4)
elif x5 >= x1 and x5 >= x2 and x5 >= x3 and x5 >= x4 and x5 >= x6:
    print(x5)
elif x6 >= x1 and x6 >= x2 and x6 >= x3 and x6 >= x4 and x6 >= x5:
    print(x6)
else:
    print(0)
