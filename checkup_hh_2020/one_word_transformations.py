# Задача 1. Преобразования слов
# Ограничение времени, с	1
# Ограничение памяти, МБ	64
#
# На вход подается 2 строки. Нужно определить, можно ли превратить первую
# строку во вторую, заменяя одни буквы на другие, с учетом следующих правил:
#
# - участвуют только буквы русского алфавита а-я;
# - все буквы в нижнем регистре;
# - за один шаг можно преобразовать все вхождения одной буквы в другую.
#
# Входные данные
# Входная информация поступает из стандартного ввода в виде одной строки.
# В этой строке содержатся две подстроки, разделенные пробелом. Ваше решение
# должно учитывать вариант, когда на вход поданы строки разной длины.
# Некорректные данные на вход не поступают, дополнительные проверки не
# требуются.
#
#
# Выходные данные
# В качестве ответа в стандартный вывод программа должна выводить 1
# (если превратить можно) или 0 (если превратить нельзя).
#
#
# Пример 1
# Входные данные: привет прикол
# Выходные данные: 1
# Преобразования (выводить не нужно):
# в ⇒ к (прикет)
# е ⇒ о (прикот)
# т ⇒ л (прикол)
#
#
# Пример 2
# Входные данные: ааббдд ддббаа
# Выходные данные: 1
# Преобразования (выводить не нужно):
# д ⇒ я (ааббяя)
# а ⇒ д (ддббяя)
# я ⇒ а (ддббаа)
#
#
# Пример 3
# Входные данные: абаб ааах
# Выходные данные: 0
# Преобразовать нельзя, так как 'б' не сможет оказаться одновременно 'а' и 'х'.

def conversions(word_one, word_two):
    if len(word_one) != len(word_two):
        return 0

    replaces = {}
    for i in range(len(word_one)):
        if word_one[i] in replaces:
            if replaces[word_one[i]] != word_two[i]:
                return 0
        replaces[word_one[i]] = word_two[i]

    if len(replaces) == 33:
        if len(set(word_two)) < 33:
            return 1
        elif word_one != word_two:
            return 0
    return 1

word_one, word_two = input().split(' ')
print(conversions(word_one, word_two))
