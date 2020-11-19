# Проценты
P, X, Y = float(input()), int(input()), int(input())
deposit_kop = X * 100 + Y
earnings = (deposit_kop * P) + 10 ** -9
deposit_kop = int(deposit_kop + earnings // 100)
print(deposit_kop // 100, deposit_kop % 100)
