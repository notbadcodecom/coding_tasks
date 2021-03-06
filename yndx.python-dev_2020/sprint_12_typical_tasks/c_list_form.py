# Вася просил Аллу помочь решить задачу. На этот раз по информатике.
#
# Для неотрицательного целого числа X списочная форма — это массив его цифр
# слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход
# подается количество цифр числа Х, списочная форма неотрицательного числа Х и
# число K. Числа К и Х не превосходят 10000.
# # Нужно вернуть списочную форму числа X + K.
#
# Формат ввода
# В первой строке - длина списочной формы числа X. На следующей строке - сама
# списочная форма с цифрами записанными через пробел. В последней строке
# записано число K.
#
# Формат вывода
# Выведите списочную форму числа X+K.
#
# Решение должно работать за O(N), где N - максимум из длин двух чисел на
# входе. Разрешается использовать O(N) дополнительной памяти.


size = int(input())
num_one = [int(i) for i in input().split(' ')]
num_two = int(input())

for i in range(size - 1, -1, -1):
    num_two += num_one[i]
    num_one[i] = num_two % 10
    num_two //= 10

while num_two != 0:
    num_one = [num_two % 10] + num_one
    num_two //= 10

print(*num_one)
