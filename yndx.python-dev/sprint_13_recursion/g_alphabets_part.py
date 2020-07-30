# Кондратий решил взяться за изучение английского языка и устроил конкурс.
# Билет на тараканьи бега получит тот, кто напишет самую быструю функцию,
# рекурсивно выводящую английский алфавит до заданной буквы включительно.
#
# Формат ввода
# На вход подается маленькая буква английского алфавита
#
# Формат вывода
# Нужно вывести ответ - алфавит с начала до заданной буквы - в строку
# через пробел.
#
#

def get_alpha_cycle(symbol, count=97): # solushion by cycle
    data = ''
    while count < ord(symbol):
        data += chr(count) + ' '
        count += 1
        if count == ord(symbol):
            data += chr(count)
    return data

def get_alpha_recursion(char, n=97, line=None):
  if line is None:
      line = []
  line.append(chr(n))
  if ord(char) == n:
      return ' '.join(line)
  return get_alpha_recursion(char, n + 1, line)


data = open('input.txt', 'r')
char = data.read()
print(get_alpha_recursion(char))
