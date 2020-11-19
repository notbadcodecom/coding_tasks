# Отсортировать список участников по алфавиту
class People:
    family = ''
    name = ''
    school_num = 0
    score = 0
input_file = open('input.txt', 'r', encoding='utf8')
output_file = open('output.txt', 'w', encoding='utf8')
people_list = []
tmp = ''
for line in input_file:
    tmp = line.split(' ')
    person = People()
    person.family = tmp[0]
    person.name = tmp[1]
    person.school_num = int(tmp[2])
    person.score = int(tmp[3])
    people_list.append(person)
people_list.sort(key=lambda man: man.family)
for person in people_list:
    print(person.family, person.name, person.score, file=output_file)
input_file.close()
output_file.close()
