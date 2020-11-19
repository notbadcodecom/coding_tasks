#  Четные индексы
def even_indices(n):
    for i in range(0, len(n), 2):
        print(n[i], end=" ")
even_indices(input().split(" "))
