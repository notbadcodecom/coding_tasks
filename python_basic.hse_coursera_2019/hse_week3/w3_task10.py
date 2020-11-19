# Удаление фрагмента
string = input()
s1 = string.find('h')
s2 = string.rfind('h') + 1
print(string[0:s1] + string[s2:len(string)])
