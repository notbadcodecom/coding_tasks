# Вечером ребята решили поиграть в игру "Большое число".
# Даны числа. Нужно определить, какое самое большое число можно из них
# составить.
#
# Формат ввода
# В первой строке записано n - количество чисел. Оно не превосходит 100.
# Во второй строке через пробел записаны n неотрицательных чисел, каждое
# из которых не превосходит 1000.
#
# Формат вывода
# Нужно вывести самое большое число, которое можно из них составить.


class LargestNum:
    class LargerKey(str):
        def __lt__(a, b):
            return a + b > b + a

    def __init__(self, nums):
        self.largest_num = sorted(nums, key=self.LargerKey)

    def __str__(self):
        return ''.join(self.largest_num)


n = int(input())
data = [i for i in input().split(' ')]
print(LargestNum(data))
