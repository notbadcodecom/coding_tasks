# Второе вхождение
s = input()
s1 = s[0:s.find('f') + 1]
s2 = s[s.find('f') + 1:len(s)]
if s1.find('f') == -1 and s2.find('f') == -1:
    print(-2)
elif s1.find('f') != -1 and s2.find('f') == -1:
    print(-1)
else:
    print(s2.find('f') + len(s1))
