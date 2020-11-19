# Задание по программированию: Сумма квадратов
natural_number = int(input())
sum_sequence = 0
i = 1
while i <= natural_number:
    sum_sequence += i**2
    i += 1
print(sum_sequence)
