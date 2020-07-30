# Чтобы выбрать самый лучший алгоритм для решения задачи,
# Гоша взялся изучать разные сортировки. На очереди - сортировка пузырьком.
#
# Алгоритм следующий (сортируем по возрастанию):
# # На каждом шаге проходим по массиву поочередно сравниваем пары соседних
# элементов. Если элемент на позиции i больше элемента на позиции j,
# меняем их местами. После первой итерации самый большой элемент окажется
# в конце массива.
#
# Проходим по массиву, выполняя указанные действия n - 1 раз, или до тех пор,
# пока на очередной итерации не окажется, что обмены больше не нужны,
# то есть массив уже отсортирован.
#
# Помогите Гоше написать код алгоритма.
#
# Формат ввода
# В первой строке на вход подается число n - длина массива. n не превосходит
# 1000. Во второй строке через пробел записаны n чисел.
# Каждое из чисел по модулю не превосходит 1000.
#
# Формат вывода
# Нужно вывести через пробел числа в отсортированном порядке.


def bubble_sort(n, data):
    flag_swapped = True
    while flag_swapped:
        flag_swapped = False
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                flag_swapped = True
    return data


n = int(input())
data = [int(i) for i in input().split(' ')]
print(*bubble_sort(n, data))
