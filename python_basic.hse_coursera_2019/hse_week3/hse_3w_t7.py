# Система линейных уравнений - 1
a, b, c, d = float(input()), float(input()), float(input()), float(input())
e, f = float(input()), float(input())
x = (e * d - b * f) / (a * d - b * c)
y = (f * a - c * e) / (a * d - b * c)
print(x, y)
