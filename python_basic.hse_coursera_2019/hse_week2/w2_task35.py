# Задание по программированию: Максимальное число подряд идущих равных
digit = ""
same_sequence = 0
count_same = 0
count_max = 0
while digit != 0:
    digit = int(input())
    if digit != same_sequence and count_max <= count_same:
        same_sequence = digit
        count_max = count_same
        count_same = 1
    elif digit != same_sequence and count_max > count_same:
        same_sequence = digit
        count_same = 1
    elif digit == same_sequence:
        count_same += 1
    else:
        continue
if count_same > count_max:
    print(count_same)
else:
    print(count_max)
