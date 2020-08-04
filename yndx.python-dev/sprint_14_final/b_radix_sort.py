# Когда Кондратий узнал про алгоритм поразрядной сортировки, он объявил конкурс
# на самую быструю реализацию алгоритма. Вы тоже принимаете участи в этом
# конкурсе. Успехов!
#
# Формат ввода
# В первой строке задано n - длина массива неотрицательных целых чисел, каждое
# из которых не превосходит 100000. # В следующей строке через пробел записаны
# n чисел.
#
# Формат вывода
# Выведите числа в отсортированном по неубыванию порядке.


def radix_sort(data, length=6):
    for i in range(length):
        lists = [[] for _ in range(10)]
        for elem in data:
            sorting_digit = elem // 10**i % 10
            lists[sorting_digit].append(elem)
        data = []
        for j in range(10):
            data += lists[j]
    return data

n = input()
data = [int(i) for i in input().split(' ')]
print(*radix_sort(data))
