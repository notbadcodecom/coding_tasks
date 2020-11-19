# Сортировка
def python_sort(n, N):
    N.sort()
    print(*N)
python_sort(int(input()), list(map(int, input().split())))
