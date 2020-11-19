# Задание по программированию: Второй максимум
digit = True
max_sequence = 0
pre_max_sequence = 0
while digit != 0:
    digit = int(input())
    if max_sequence > digit > pre_max_sequence:
        pre_max_sequence = digit
    elif digit > max_sequence:
        pre_max_sequence = max_sequence
        max_sequence = digit
    elif digit == max_sequence:
        pre_max_sequence = digit
    else:
        continue
print(pre_max_sequence)
