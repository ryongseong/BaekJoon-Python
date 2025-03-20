import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]


def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    dist = [[float("inf")] * M for _ in range(N)]
    dist[0][0] = 0

    while pq:
        cost, r, c = heapq.heappop(pq)

        if (r, c) == (N - 1, M - 1):
            return cost

        if cost > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                new_cost = cost + matrix[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    return -1


print(dijkstra())
