#  Переставить min и max
def rearrange(n):
    min_n, max_n = n[0], n[0]
    min_i, max_i = 0, 0
    for i in range(len(n)):
        if n[i] < min_n:
            min_n = n[i]
            min_i = i
        elif n[i] > max_n:
            max_n = n[i]
            max_i = i
    n[max_i], n[min_i] = n[min_i], n[max_i]
    print(*n)
rearrange(list(map(int, input().split())))
