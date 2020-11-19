# Сортировка подсчетом
def CountSort(A):
    count_A = [0] * (max(A) + 1)
    for a in A:
        count_A[a] += 1
    for now in range(len(count_A)):
        print((str(now) + ' ') * count_A[now], end='')


CountSort(list(map(int, input().split())))
