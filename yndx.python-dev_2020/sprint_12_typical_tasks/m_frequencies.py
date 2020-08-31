# А теперь помогите Васе решить задачу по информатике. Он снова томится дома
# в хорошую погоду.
#
# На вход подается строка длиной от 1 до 10000 символов. Нужно отсортировать
# её в порядке частот букв по встречаемости. Заглавные и строчные буквы
# считаются разными. Если частота одинаковая, нужно применить вторичную
# сортировку лексикографически.
#
# Формат ввода
# Одна строка длиной не более 10000 символов.
#
# Формат вывода
# Строка, в которой символы отсортированы в порядке убывания частотности.

letters_in = input()
letters_cnt = {}
counts = {}
numbers = set()
letters_out = ''

for letter in letters_in:
    if letter in letters_cnt:
        letters_cnt[letter] += 1
    else:
        letters_cnt[letter] = 1

for key, value in letters_cnt.items():
    if value in counts:
        counts[value].append(key * value)
    else:
        counts[value] = [key] * value
    numbers.add(value)
numbers = sorted(numbers, reverse=True)

for number in numbers:
    letters_out += ''.join((sorted(counts[number])))

print(letters_out)
