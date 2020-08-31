# Руководство компании, где работают Гоша с друзьями, подарило каждому
# сотруднику два талона на обед в близлежащем ресторане. Сотрудники могли
# взять талоны и записать номер своего бейджика в специальный бланк.
# Так сделали все кроме одного сотрудника. Нужно вычислить, кто же это такой!
# На вход подается непустой массив целых чисел. Каждое из них, за исключением
# одного, встречается 2 раза. Размер массива не превосходит 10000. Числа по
# модулю не больше 10000. Нужно выяснить, кто не такой, как все!
#
# Формат ввода
# В первой строке записано число n. Во второй строке через пробел записаны n
# чисел. Длина массива и каждое из чисел не превосходят 10000.
#
# Формат вывода
# Выведите единственное число, соответствующее id отличившегося сотрудника

employees = int(input())
coupons = input().split(' ')
coupons_count = {}
for coupon in coupons:
    coupons_count[coupon] = coupons_count.get(coupon, 0) + 1
for key, value in coupons_count.items():
    if value != 2:
        print(key)
