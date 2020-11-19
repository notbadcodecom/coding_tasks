# Количество нулей
def isZero(N):
    countZero = 0
    for i in range(N):
        digit = int(input())
        if digit == 0:
            countZero += 1
    return countZero
print(isZero(int(input())))
