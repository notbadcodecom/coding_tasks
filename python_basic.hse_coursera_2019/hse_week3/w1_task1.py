# Задание по программированию: Площадь треугольника
a, b, c = float(input()), float(input()), float(input())
p = 1 / 2 * (a + b + c)
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('{0:.6f}'.format(S))
