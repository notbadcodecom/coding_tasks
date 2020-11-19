#  Переставить соседние
def change_last(A):
    for i in range(0, len(A) - len(A) % 2, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    print(*A)
change_last(list(map(int, input().split())))
