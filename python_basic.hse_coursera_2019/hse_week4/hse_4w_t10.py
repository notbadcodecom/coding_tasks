# Сумма последовательности
def sumSequence():
    digit = int(input())
    if digit == 0:
        return 0
    return digit + sumSequence()
print(sumSequence())
