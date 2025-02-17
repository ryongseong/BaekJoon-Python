import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1]*(V+1)
    visited[start] = True
    result = [0, 0]

    while q:
        node, cost = q.popleft()

        for n_node, n_cost in edges[node]:
            if visited[n_node] == -1:
                now_cost = cost + n_cost
                q.append((n_node, now_cost))
                visited[n_node] = now_cost
                if result[1] < now_cost:
                    result = [n_node, now_cost]
    
    return result


V = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(V):
    line = list(map(int, input().split()))
    node = line[0]
    idx = 1
    while line[idx] != -1:
        n_node, n_cost = line[idx], line[idx+1]
        edges[node].append((n_node, n_cost))
        idx += 2

p, a = bfs(1)
print(bfs(p)[1])