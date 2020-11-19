#  Больше предыдущего
def least_positive(n):
    positive_digit = 1000
    for i in range(len(n)):
        if int(n[i]) > 0 and int(n[i]) < positive_digit:
            positive_digit = int(n[i])
    print(positive_digit)
least_positive(input().split())
