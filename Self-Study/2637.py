from collections import deque

N = int(input())
M = int(input())

edges = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
answer = [0] * (N + 1)
answer[N] = 1

for _ in range(M):
    x, y, k = map(int, input().split())
    edges[x].append((y, k))
    indegree[y] += 1

queue = deque([N])
origin = [i for i in range(1, N + 1) if not edges[i]]

while queue:
    node = queue.popleft()
    for next_node, cnt in edges[node]:
        indegree[next_node] -= 1
        answer[next_node] += cnt * answer[node]
        if not indegree[next_node]:
            queue.append(next_node)

for i in origin:
    print(i, answer[i])
