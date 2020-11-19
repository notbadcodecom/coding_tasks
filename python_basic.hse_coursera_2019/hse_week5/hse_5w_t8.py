#  Количество положительных
def positive_element(n):
    count = 0
    for i in range(len(n)):
        if int(n[i]) > 0:
            count += 1
    print(count)
positive_element(input().split(" "))
