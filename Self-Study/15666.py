N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))

result = [0] * M


def sol(k, idx):
    if k == M:
        for i in range(M):
            print(result[i], end=" ")
        print()
        return

    temp = 0
    for i in range(idx, N):
        if temp != data[i]:
            result[k] = data[i]
            temp = data[i]
            sol(k + 1, i)


sol(0, 0)
