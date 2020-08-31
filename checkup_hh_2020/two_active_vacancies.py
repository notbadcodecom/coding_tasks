# Задача 2. Активные вакансии
#
# # Ограничение времени, с	2
# Ограничение памяти, МБ	96
#
# Петя решил узнать, когда программисту выгоднее всего искать работу на hh.ru.
# Конечно, когда больше всего открыто вакансий.
#
# Он выгрузил в текстовый файл время открытия и закрытия всех подходящих
# вакансий за 2019 год.
#
# Теперь нужно определить период времени, когда открытых вакансий было больше
# всего.
#
# Считаем, что:
# - начальное и конечное время всегда присутствуют;
# - начальное время всегда меньше или равно конечному;
# - начальное и конечное время включены в интервал.
#
# Входные данные
# Входная информация поступает из стандартного ввода, в первой строке приходит
# 1 число - количество вакансий. Каждая из следующих строк содержит информацию
# о вакансии в виде двух чисел – начальное и конечное время, они разделены
# пробелом. Время задается в секундах (https://ru.wikipedia.org/wiki/Unix-время).
# Некорректные данные на вход не поступают, дополнительные проверки не требуются.
#
# # Выходные данные
# В качестве ответа в стандартный вывод через пробел нужно вывести два числа:
# количество найденных интервалов и сумму длительности интервалов в секундах
# (начальная и конечная секунды должны быть включены в интервал).
#
# # Пример 1
# Входные данные:
# 1
# 1595862781 1595862785
# Выходные данные: 1 5
#
# # Пример 2
# Входные данные:
# 2
# 1595862781 1595862783
# 1595862782 1595862784
# Выходные данные: 1 2
#
# # Пример 3
# Входные данные:
# 2
# 1595862781 1595862782
# 1595862783 1595862784
# Выходные данные: 2 4


def get_spans(timestamps):
    vacancies, time_sum, spans, flag, vacancies_max = [0 for _ in range(5)]
    vacancies_current = None

    for i in range(len(timestamps)):
        if not timestamps[i][1]:
            vacancies += 1
            if vacancies > vacancies_max:
                flag = True
                vacancies_max = vacancies
        elif timestamps[i][1]:
            vacancies -= 1
            if vacancies < vacancies_max and flag:
                span = timestamps[i][0] - timestamps[i - 1][0] + 1
                if vacancies_current is None:
                    vacancies_current = vacancies_max
                if vacancies_max > vacancies_current:
                    vacancies_current = vacancies_max
                    time_sum = span
                    spans = 1
                elif vacancies_max == vacancies_current:
                    time_sum += span
                    spans += 1
                vacancies_max = vacancies
    return [spans, time_sum]


timestamps = []
for _ in range(int(input())):
    start, end = map(int, input().split(' '))
    timestamps.append([start, False])
    timestamps.append([end, True])
timestamps = sorted(timestamps)

print(*get_spans(timestamps))
