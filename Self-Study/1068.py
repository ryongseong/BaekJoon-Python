def dfs(num, parents):
    parents[num] = -2
    for i in range(N):
        if num == parents[i]:
            dfs(i, parents)


N = int(input())
parents = list(map(int, input().split()))
remove_idx = int(input())
cnt = 0

dfs(remove_idx, parents)
for i in range(N):
    if parents[i] != -2 and i not in parents:
        cnt += 1

print(cnt)
