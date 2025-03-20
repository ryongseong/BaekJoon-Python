from heapq import heappop, heappush


def prim(start_node):
    pq = [(0, start_node)]
    visited = [0] * N
    min_cost = 0

    while pq:
        weight, node = heappop(pq)

        if visited[node]:
            continue
        visited[node] = 1
        min_cost += weight

        for next_node in range(N):
            if not graph[node][next_node]:
                continue
            if visited[next_node]:
                continue

            heappush(pq, (graph[node][next_node], next_node))

    return min_cost


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
print(prim(0))
