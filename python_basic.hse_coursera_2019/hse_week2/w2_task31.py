# Задание по программированию: Количество четных элементов последовательности
number = 1
i = -1
while number > 0:
    number = int(input())
    if number % 2 == 0:
        i += 1
    else:
        continue
print(i)
