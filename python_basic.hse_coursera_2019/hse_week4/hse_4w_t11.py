# Разворот последовательности
def reversalSequence():
    digit = int(input())
    if digit != 0:
        reversalSequence()
    print(digit)
reversalSequence()
