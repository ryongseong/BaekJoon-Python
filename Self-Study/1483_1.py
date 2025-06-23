import heapq


def get_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


N = int(input())
town_points = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N - 1):
    dist = get_dist(town_points[i], town_points[i + 1])
    graph[i].append((i + 1, dist))
    graph[i + 1].append((i, dist))

sort_by_x_point_list = sorted((x, i) for i, (x, _) in enumerate(town_points))
sort_by_y_point_list = sorted((y, i) for i, (_, y) in enumerate(town_points))

for i in range(N - 1):
    x1, x2 = sort_by_x_point_list[i][1], sort_by_x_point_list[i + 1][1]
    dist = get_dist(town_points[x1], town_points[x2])
    graph[x1].append((x2, dist))
    graph[x2].append((x1, dist))

for i in range(N - 1):
    y1, y2 = sort_by_y_point_list[i][1], sort_by_y_point_list[i + 1][1]
    dist = get_dist(town_points[y1], town_points[y2])
    graph[y1].append((y2, dist))
    graph[y2].append((y1, dist))

costs = [float("inf")] * N
costs[0] = 0

pq = [(0, 0)]

while pq:
    node, cost = heapq.heappop(pq)
    if cost > costs[node]:
        continue

    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        if costs[next_node] > new_cost:
            costs[next_node] = new_cost
            heapq.heappush(pq, (next_node, new_cost))

print(costs[N - 1])
