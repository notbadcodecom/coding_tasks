# Задача 2
# Есть несортированный массив из целых чисел.
# Есть целое число X.
# Нужно найти, есть ли в нем два элементас разными значениями таких,
# что A1 + A2 = X
# Ограничений по памяти нет.
# По времени - чем быстрее, тем лучше.


def get_sum(data, x, start=0):
    arr = sorted(data)
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == x and arr[start] != arr[end]:
            return arr[start], arr[end]
        elif arr[start] + arr[end] < x:
            start += 1
        else:
            end -= 1
    return 'no solution'
