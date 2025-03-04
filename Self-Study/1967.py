import sys

sys.setrecursionlimit(10**9)


def dfs(start, cost):
    for next_node, next_cost in tree[start]:
        if visited[next_node] == -1:
            visited[next_node] = cost + next_cost
            dfs(next_node, cost + next_cost)


n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

last_node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[last_node] = 0
dfs(last_node, 0)

print(max(visited))
