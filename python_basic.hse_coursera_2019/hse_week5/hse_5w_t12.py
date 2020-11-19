#  Ближайшее число
def nearest_digit(N):
    massive = list(map(int, input().split()))
    massive2 = []
    digit = int(input())
    for i in range(N):
        massive2.append((massive[i] - digit) * (massive[i] - digit))
    min_digit = massive2[0]
    min_index = 0
    for i in range(N - 1):
        if min_digit >= massive2[i + 1]:
            min_digit = massive2[i + 1]
            min_index = i + 1
    print(massive[min_index])
nearest_digit(int(input()))
