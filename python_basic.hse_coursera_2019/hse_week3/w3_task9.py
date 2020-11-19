# Первое и последнее вхождение
string = input()
if string.find('f') >= 0:
    num1 = string.find('f')
else:
    num1 = ""
if string.rfind('f') != 0 and string.rfind('f') == string.find('f'):
    num2 = ""
elif string.rfind('f') != 0:
    num2 = string.rfind('f')
print(num1, num2)
