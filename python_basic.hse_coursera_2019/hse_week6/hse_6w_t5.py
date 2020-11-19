# Гражданская оборона
def civil_protection():
    n = int(input())
    villages, shelters, data = [], [], []
    tmp = list(map(int, input().split()))
    for i in range(n):
        villages.append((tmp[i], i + 1))
    villages.sort()
    m = int(input())
    tmp = list(map(int, input().split()))
    for i in range(m):
        shelters.append((tmp[i], i + 1))
    shelters.sort()
    j = 0
    tmp = []
    for i in range(n):
        while j < m:
            if j == (m - 1):
                x = (villages[i][0] - shelters[j][0]) ** 2
                y = (villages[i][0] - shelters[j - 1][0]) ** 2
                if x < y:
                    tmp.append((villages[i][1], shelters[j][1]))
                    break
                else:
                    tmp.append((villages[i][1], shelters[j - 1][1]))
                    break
            x = (villages[i][0] - shelters[j][0])**2
            y = (villages[i][0] - shelters[j + 1][0])**2
            if x <= y:
                tmp.append((villages[i][1], shelters[j][1]))
                break
            elif x > y:
                j += 1
    tmp.sort()
    for i in range(n):
        data.append(tmp[i][1])
    print(*data)
civil_protection()
