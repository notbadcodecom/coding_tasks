#  Четные элементы
def even_elements(n):
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            print(n[i], end=" ")
even_elements(input().split(" "))
