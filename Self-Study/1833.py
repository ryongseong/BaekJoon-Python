def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA
        return True
    return False


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

graph = []
total_remove_cost = 0

for i in range(n):
    for j in range(n):
        if i < j:
            val = matrix[i][j]
            if val < 0:
                total_remove_cost += -val
                graph.append((0, i, j, "keep"))
            elif val > 0:
                graph.append((val, i, j, "build"))

graph.sort()
parent = list(range(n))
result_cost = 0
result_ops = []

for cost, a, b, op_type in graph:
    if union(parent, a, b):
        result_cost += cost
        if op_type == "build":
            result_ops.append((a + 1, b + 1))

print(total_remove_cost + result_cost, len(result_ops))
for line in result_ops:
    print(*line)
