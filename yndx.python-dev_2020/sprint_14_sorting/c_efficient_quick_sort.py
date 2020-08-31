# Рита захотела оптимизировать алгоритм быстрой сортировки. Алгоритму не должно
# требоваться O(n) дополнительной памяти. А у вас получится?
#
# Формат ввода
# В первой строке на вход подается число n - длина массива. n не превосходит
# 1000. Во второй строке через пробел записаны n чисел. Каждое из чисел по
# модулю не превосходит 1000.
#
# Формат вывода
# Нужно вывести через пробел числа в отсортированном по возрастанию порядке.

def partition(array, low, high):
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


n = int(input())
data = [int(i) for i in input().split()]
quick_sort(data)
print(*data)
