# Проходной балл
input_file = open('input.txt', 'r', encoding='utf8')
output_file = open('output.txt', 'w', encoding='utf8')
score = []
index = 0
for line in input_file:
    tmp = line.split(' ')
    if len(tmp) == 1:
        K = int(tmp[0])
    elif int(tmp[-3]) >= 40 and int(tmp[-2]) >= 40 and int(tmp[-1]) >= 40:
        score.append((int(tmp[-3]) + int(tmp[-2]) + int(tmp[-1])))
        index += 1
    else:
        score.append(0)
score.sort(reverse=1)
index_score = []
count = -1
for i in range(len(index_score)):
    count += index_score[i]
if len(index_score) == 0:
    print(1, file=output_file)
elif index <= K:
    print(0, file=output_file)
else:
    count = 0
    for i in range(K):
        if score[i] > score[i + 1]:
            count += 1
            index_score.append(count)
            count = 0
        elif score[i] == score[i + 1]:
            count += 1
    print(score[count], file=output_file)
input_file.close()
output_file.close()
