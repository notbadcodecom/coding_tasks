# Алла писала код, добавляющий запись в новую таблицу базы данных. И вдруг
# получила ошибку duplicate foreign key constraint. В тот же момент её отвлекла
# Рита. Алла случайно закрыла окно терминала с информацией о том, какое именно
# значение стало причиной ошибки. Зато у неё сохранился список id,
# использованных при запросе. Помогите ей выяснить, какой id стал причиной
# ошибки.
#
# Дан массив чисел, состоящий  из n целых чисел. Одно число встречается более
# одного раза. Нужно определить это число.
#
# Формат ввода
# В первой строке записано число n, которое не превосходит 1000. В следующей
# строке через пробел записаны n целых чисел, каждое из которых также не
# превосходит 10000.
#
# Формат вывода
# Выведите одно число.


n = int(input())
data = [int(i) for i in input().split(' ')]

for i in range(n):
    if data[i] in data[:i]:
        print(data[i])
