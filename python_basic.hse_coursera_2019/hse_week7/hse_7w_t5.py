# Угадай число
Beatrice = 0
array = set()
n = int(input())
for i in range(1, n + 1):
    array.add(i)
i = len(array)
while i != 1:
    Beatrice = input()
    if Beatrice == 'HELP':
        i = 1
    else:
        August = input()
        question = set(map(int, Beatrice.split()))
        i = len(array)
        if August == 'NO':
            array -= question
        else:
            array &= question
print(*sorted(array))
