# В метро Гоша обычно играет в мобильную игру «Черепашенька». Он долго собирал
# данные о том, сколько очков зарабатывает и проигрывает в день. Гоша собирает
# необычную статистику. Нужно определить максимальное произведение заработанных
# очков среди троек дней, в которые сумма очков равна нулю, и произведение
# является положительным числом.
#
# Формат ввода
# В первой строке записано число n (1 ≤ n ≤ 2000). В следующей строке через
# пробел записаны n целых чисел. Числа находятся в диапазоне от -10000 до 10000
#
# Формат вывода
# Выведите максимальное положительное произведение заработанных за три дня
# очков среди троек дней, в которые их сумма равна нулю. Если троек,
# удовлетворяющих условиям, нет, нужно вывести -1.
#
# Примечания
# Решение должно использовать O(1) дополнительной памяти (помимо массива, в
# который считаны входные данные).


n = int(input())
data = [int(i) for i in input().split(' ')]
data = sorted(data)

score_max = -1
for i in range(len(data) - 2):
    left = i + 1
    right = len(data) - 1
    flag = True
    while left < right:
        check = data[left] + data[i] + data[right]
        if check == 0:
            check = data[left] * data[i] * data[right]
            if check > score_max:
                score_max = check
            left += 1
            right -= 1
            break
        elif check > 0:
            right -= 1
        else:
            left += 1

print(score_max)