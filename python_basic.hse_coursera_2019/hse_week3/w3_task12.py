# Переставить два слова
s = input()
w1 = s[0:s.find(' ')]
w2 = s[s.find(' ') + 1:len(s)]
print(w2, w1)
