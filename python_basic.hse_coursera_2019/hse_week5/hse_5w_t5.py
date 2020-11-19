# Лесенка
def ladder(n):
    for i in range(1, n + 1):
        stepLadder = ()
        for j in range(1, i + 1):
            stepLadder += (j,)
        print(*stepLadder, sep="")
ladder(int(input()))
