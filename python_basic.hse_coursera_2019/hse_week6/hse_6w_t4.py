# Создание архива
def creation_archive(SN):
    V, N, S, S_max, i = [], SN[1], SN[0], 0, 0
    for i in range(N):
        V.append(int(input()))
    V.sort()
    for i in range(N):
        S_max += V[i]
        if S_max > S:
            i -= 1
            break
        elif S_max == S or (S_max < S and i == N):
            break
    print(i + 1)
creation_archive(list(map(int, input().split())))
