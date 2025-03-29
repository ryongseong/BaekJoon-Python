import heapq
import sys
import bisect

input = sys.stdin.readline


def solve(N, M, K, L, blackholes):
    directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

    rows = sorted(rk - 1 for rk, ck in blackholes)
    cols = sorted(ck - 1 for rk, ck in blackholes)

    prefix_rows = [0] * (K + 1)
    for i in range(K):
        prefix_rows[i + 1] = prefix_rows[i] + rows[i]
    prefix_cols = [0] * (K + 1)
    for i in range(K):
        prefix_cols[i + 1] = prefix_cols[i] + cols[i]

    def row_cost(i):
        pos = bisect.bisect_left(rows, i)
        left_count = pos
        right_count = K - pos
        return (
            i * left_count
            - prefix_rows[pos]
            + (prefix_rows[K] - prefix_rows[pos])
            - i * right_count
        )

    def col_cost(j):
        pos = bisect.bisect_left(cols, j)
        left_count = pos
        right_count = K - pos
        return (
            j * left_count
            - prefix_cols[pos]
            + (prefix_cols[K] - prefix_cols[pos])
            - j * right_count
        )

    row_costs = [row_cost(i) for i in range(N)]
    col_costs = [col_cost(j) for j in range(M)]

    def t_value(x, y):
        return row_costs[x] + col_costs[y]

    dist = [[[float("inf")] * (L + 1) for _ in range(M)] for _ in range(N)]
    dist[0][0][0] = 0

    pq = [(0, 0, 0, 0, "")]
    while pq:
        cost, x, y, steps, path = heapq.heappop(pq)
        if steps == L:
            if x == N - 1 and y == M - 1:
                return path
            continue

        for dx, dy, d in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                new_cost = cost + abs(t_value(x, y) - t_value(nx, ny))
                if dist[nx][ny][steps + 1] > new_cost:
                    dist[nx][ny][steps + 1] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, steps + 1, path + d))
    return -1


N, M, K, L = map(int, input().split())
blackholes = [tuple(map(int, input().split())) for _ in range(K)]
print(solve(N, M, K, L, blackholes))
