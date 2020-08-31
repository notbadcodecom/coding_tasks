# Помогите жителям Трешландии понять, сколько питомцев они могут завести.
# Напишите рекурсивную реализацию функции, определяющей по номеру
# значение n-ого числа Фибоначчи.

# Формат ввода
# На вход подается n - целое число в диапазоне от 0 до 30.
#
# Формат вывода
# Нужно вывести n-ое число Фибоначчи.


def get_fibonacci_number(n):
    if n <= 1:
        return 1
    fibonacci_number = get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)
    return fibonacci_number


data = open('input.txt', 'r')
n = int(data.read())
print(get_fibonacci_number(n))

