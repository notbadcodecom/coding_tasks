# Количество элементов, равных максимуму
digit = True
max_sequence = 0
count_max_sequence = 0
while digit != 0:
    digit = int(input())
    if digit > max_sequence:
        max_sequence = digit
        count_max_sequence = 1
    elif digit == max_sequence:
        count_max_sequence += 1
    else:
        continue
print(count_max_sequence)
