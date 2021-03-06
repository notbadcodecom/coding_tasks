# К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
# Но не всё так просто. Печенья могут быть разного размера. У каждого ребёнка
# есть фактор жадности — минимальный размер печенья, которое он возьмёт.
# Нужно выяснить, сколько ребят останутся довольными.
# Каждый ребёнок может взять не больше одного печенья.
#
# Формат ввода
# В первой строке записано n - количество детей.
# Во второй - n чисел, разделенных пробелом - фактор жадности
# для каждого ребенка, целое число, не превосходящее 1000.
# В следующей строке записано - m - количество печенек.
# Далее - m чисел, разделенных пробелом - размеры печенек.
# Оба числа n и m не превосходят 10000.
#
# Формат вывода
# Нужно вывести одно число — количество детей, которые останутся довольными


def get_satisfied(n, m, greeds, sizes, j=0, i=0, count=0):
    while i < m and j < n:
        if greeds[j] <= sizes[i]:
            count += 1
            j += 1
        i += 1
    return count

n = int(input())
greeds = sorted([int(greed) for greed in input().split(' ')])
m = int(input())
sizes = sorted([int(size) for size in input().split(' ')])
print(get_satisfied(n, m, greeds, sizes))






