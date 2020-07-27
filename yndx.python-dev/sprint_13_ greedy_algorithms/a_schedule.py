# Помогите Алле написать код алгоритма для выбора уроков,
# которые пройдут в классе. Дано расписание предметов.
# Нужно составить расписание, в соответствии с которым
# в классе можно будет провести как можно больше уроков.
#
# Формат ввода
# В первой строке задано число предметов. Оно не превосходит 1000.
# Далее для каждого предмета в отдельной строке записано время начала
# и окончания урока. Обратите внимание на формат времени.
# Указываются только значащие цифры.
#
# Формат вывода
# Выведите информацию о всех уроках, которые нужно провести в кабинете,
# в порядке возрастания времени начала.
#
# Примечания
# Если возможно несколько оптимальных вариантов, нужно выбирать урок,
# у которого начало раньше. # Возможно проведение более чем одного урока
# нулевой длительности одновременно.


class Lesson:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        start, end = timestamp.split(' ')
        self.start = self.convert_minutes(start)
        self.end = self.convert_minutes(end)
        self.lenght = self.end * 2 + self.start

    def convert_minutes(self, time):
            return (int(float(time) * 100) % 100) + int(float(time)) * 60

    def __repr__(self):
            return str(self.timestamp)


def get_schedule(n, lessons):
    lessons.sort(key=lambda item: item.lenght)
    schedule = [lessons[0]]
    for lesson in lessons:
        peek = schedule[len(schedule) - 1]
        if lesson is peek:
            continue
        elif lesson.start >= peek.end:
            schedule.append(lesson)
        elif lesson.end < peek.end:
            schedule.pop()
            schedule.append(lesson)
    return [len(schedule)] + schedule


n = int(input())
lessons = [Lesson(input()) for _ in range(n)]
for elem in get_schedule(n, lessons):
    print(elem)
