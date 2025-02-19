from copy import deepcopy
import sys
from collections import deque
input = sys.stdin.readline

directions = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]


def bfs():
    global result
    tmp_graph = deepcopy(graph)

    queue = deque()
    
    for r in range(N):
        for c in range(M):
            if tmp_graph[r][c] == 2:
                queue.append((r, c))
    
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if tmp_graph[nr][nc] == 0:
                tmp_graph[nr][nc] = 2
                queue.append((nr, nc))
    cnt = 0
    for i in range(N):
        cnt += tmp_graph[i].count(0)
    
    result = max(result, cnt)


def make(cnt):
    if cnt == 3:
        bfs()
        return

    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                graph[r][c] = 1
                make(cnt + 1)
                graph[r][c] = 0


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
make(0)
print(result)