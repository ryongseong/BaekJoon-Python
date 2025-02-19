import sys
input = sys.stdin.readline

def sol():
    check = 0
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        if check != arr[i] and visited[i] == 0:
            result.append(arr[i])
            visited[i] = 1
            check = arr[i]
            sol()
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))
visited = [0 for _ in range(N)]
result = []
sol()
