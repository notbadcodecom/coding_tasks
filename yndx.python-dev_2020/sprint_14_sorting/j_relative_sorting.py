# Кондратий ввел новый метод сортировки - Относительная сортировка.
# Идея метода следующая. С помощью образца - массива уникальных чисел,
# задается порядок. В соответствии с этим порядком и должны сортироваться
# числа. # Но метод еще требует доработки. Пока не известно, как сортировать
# числа, которые не входят в образец. Так что такие числа нужно выводить в
# конце в соответствии со стандартной сортировкой.
#
# Формат ввода
# В первой строке задано количество чисел, которые нужно отсортировать, n.
# Оно не превосходит 1000. # В следующей строке через пробел заданы n чисел,
# каждое из которых не превосходит 1000. В третей строке задана длина
# образца m. Это число не превосходит 1000. В следующей строке записан образец.
# Он состоит из чисел, не превосходящих 1000. Гарантируется, что среди чисел,
# которые нужно отсортировать, присутствуют все числа из образца.
#
# Формат вывода
# Выведите в строку через пробел числа, отсортированные
# относительной сортировкой.


def relative_sorting(elements, pattern):
    if pattern is None:
        return sorted(elements)

    comparison = set(pattern)
    head = [0] * (max(pattern) + 1)
    tail = []
    for elem in elements:
        if elem in comparison:
            head[elem] += 1
        else:
            tail.append(elem)

    data = []
    for elem in pattern:
        data += head[elem] * [elem]
    data += sorted(tail)
    return data


n = int(input())
if n != 0:
    data_list = [int(i) for i in input().split()]
else:
    data_list = []
m = int(input())
if m == 0:
    data_pattern = None
else:
    data_pattern = [int(i) for i in input().split()]
print(*relative_sorting(data_list, data_pattern))
