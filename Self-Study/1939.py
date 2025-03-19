import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end, weight):
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        node = queue.popleft()

        if node == end:
            return True

        for neighbor, limit in graph[node]:
            if neighbor not in visited and limit >= weight:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_weight = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_weight = max(max_weight, c)

start, end = map(int, input().split())

left, right = 1, max_weight
result = left

while left <= right:
    mid = (left + right) // 2
    if bfs(start, end, mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
