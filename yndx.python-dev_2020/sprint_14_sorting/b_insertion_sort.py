# Теперь Гоша взялся за сортировку вставками.
# # Алгоритм следующий: На i-том шаге мы делаем так, чтобы первые i элементов
# массива шли в возрастающем порядке.
#
# 1) На первом шаге ничего делать не нужно - один элемент и так "отсортирован".
# 2) На втором шаге нужно сделать так, чтобы два первых элемента были верно
# отсортированы. То есть если второй элемент оказался меньше первого, их нужно п
# оменять местами.
# # 3) На i - том шаге мы знаем, что первые i-1 элементов уже отсортированы.
# Ищем, куда нужно вставить i-ый элемент.
# # Для этого, начиная с позиции j = i - 1, сравниваем текущий элемент с
# элементом на позиции j. Пока j - й элемент больше i-ого и j > 0, меняем
# элементы местами, и уменьшаем счетчик j на 1.
#
# Помогите Гоше написать код.
#
# Формат ввода
# В первой строке на вход подается число n - длина массива. n не превосходит
# 1000. Во второй строке через пробел записаны n чисел. Каждое из чисел по
# модулю не превосходит 1000.
#
# Формат вывода
# Нужно вывести через пробел числа в отсортированном по возрастанию порядке.


def insertion_sort(n, data):
    for i in range(1, n):
        insertion_elem = data[i]
        j = i - 1
        while j >= 0 and insertion_elem < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = insertion_elem
    return data


n = int(input())
data = [int(i) for i in input().split()]
print(*insertion_sort(n, data))
