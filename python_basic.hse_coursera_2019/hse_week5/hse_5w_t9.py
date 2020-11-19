#  Последний максимум
def last_max(n):
    max_index = 0
    max_digit = int(n[0])
    for i in range(len(n) - 1):
        if max_digit <= int(n[i + 1]):
            max_digit = int(n[i + 1])
            max_index = i + 1
    print(max_digit, max_index)
last_max(input().split())
