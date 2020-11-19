# Задание по программированию: Максимум последовательности
digit = ""
max_sequence = 0
while digit != 0:
    digit = int(input())
    if digit > max_sequence:
        max_sequence = digit
print(max_sequence)
