# Слияние списков
def merge(A, B):
    j, k, C = 0, 0, []
    for i in range(len(A + B)):
        if j < len(A) and k < len(B):
            if A[j] < B[k]:
                C.append(A[j])
                j += 1
            else:
                C.append(B[k])
                k += 1
        elif j == len(A):
            C = C + (B[k:len(B)])
            break
        else:
            C = C + (A[j:len(A)])
            break
    return C
print(*merge(list(map(int, input().split())), list(map(int, input().split()))))
