# Ряд - 2
def rangeTwo(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(i, end=" ")
    else:
        for i in range(a, b - 1, -1):
            print(i, end=" ")
rangeTwo(int(input()), int(input()))
