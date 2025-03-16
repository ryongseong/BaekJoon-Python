def dfs(arr, lev):
    mid = len(arr) // 2
    result[lev].append(arr[mid])

    if len(arr) == 1:
        return

    dfs(arr[:mid], lev + 1)
    dfs(arr[mid + 1 :], lev + 1)


k = int(input())
data = list(map(int, input().split()))
result = [[] for _ in range(k)]
dfs(data, 0)

for r in result:
    print(*r)
