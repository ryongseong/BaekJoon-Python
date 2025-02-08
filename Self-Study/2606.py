n = int(input())

varius = [False] * (n + 1)
pair_count = int(input())

pairs = sorted([list(map(int, input().split())) for _ in range(pair_count)])

def dfs(node):
    varius[node] = True
    for a, b in pairs:
        if a == node and not varius[b]:
            dfs(b)
        elif b == node and not varius[a]:
            dfs(a)

dfs(1)
print(varius.count(True) - 1)