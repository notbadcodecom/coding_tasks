# Номер появления слова
input_file = open('input.txt', 'r', encoding='utf8')
txt = []
dict = {}
tmp = []
for line in input_file:
    txt += (line.split())
for word in txt:
    dict[word] = dict.get(word, -1) + 1
    print(dict[word], end=' ')
