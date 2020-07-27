# Функция из прошлого задания работала слишком долго.
# Нужно модифицировать ее таким образом, чтобы одни и
# те же значения повторно не вычислялись.
#
# Формат ввода
# На вход подается число n.
#
# Формат вывода
# Напечатайте n-ное число Фибоначчи.

def get_fibonacci_number(pos):
    if pos == 0:
        data = [1, 0]
    else:
        fib_two, fib_one = get_fibonacci_number(pos - 1)
        data = [fib_two + fib_one, fib_two]
    if pos == n:
        return data[0]
    return data


data = open('input.txt', 'r')
n = int(data.read())
print(get_fibonacci_number(n))
