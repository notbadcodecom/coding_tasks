#  Больше предыдущего
def last_more(n):
    for i in range(len(n) - 1):
        if int(n[i]) < int(n[i + 1]):
            print(n[i + 1], end=" ")
last_more(input().split())
