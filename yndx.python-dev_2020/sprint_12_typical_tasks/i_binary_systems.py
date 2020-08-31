# Тимофей спросил у студента Саши, умеет ли тот работать с числами в двоичной
# системе счисления. Он ответил, что проходил это на одной из первых лекций по
# информатике. Тимофей предложил Саше решить задачку. Два числа записаны в
# двоичной системе счисления. Нужно вывести их сумму, также в двоичной системе.
# Встроенную в язык программирования возможность сложения двоичных чисел
# рименять нельзя.
#
# Формат ввода
# Два числа в двоичной системе счисления, каждое на отдельной строке.
#
# Формат вывода
# Одно число в двоичной системе счисления.
#
# Примечания
# Решение должно работать за O(N) и использовать O(N) дополнительной памяти,
# где N - количество разрядов максимального числа на входе.

binary_one = input()
binary_two = input()
binary_sum = ''

if len(binary_two) > len(binary_one):
    binary_one, binary_two = binary_two, binary_one

max_len = len(binary_one)
min_len = len(binary_two)
rank = 0

while min_len > 0:
    amount = int(binary_one[max_len - 1]) + int(binary_two[min_len - 1]) + rank
    binary_sum = str(amount & 1) + binary_sum
    rank = amount >> 1
    max_len -= 1
    min_len -= 1

while max_len > 0:
    amount = int(binary_one[max_len - 1]) + rank
    binary_sum = str(amount & 1) + binary_sum
    rank = amount >> 1
    max_len -= 1

if rank == 1:
    binary_sum = '1' + binary_sum

print(binary_sum)
