import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline


def dijkstra(graph, costlist, s):
    minload = [[] for x in range(n)]
    queue = deque([(s, 0)])
    costlist[s] = 0
    while queue:
        node, cost = queue.popleft()
        if cost > costlist[node]:
            continue
        for next_node, next_cost in graph[node]:
            if next_cost != -1:
                if costlist[next_node] > costlist[node] + next_cost:
                    costlist[next_node] = costlist[node] + next_cost
                    minload[next_node].clear()
                    minload[next_node].append(node)
                    queue.append((next_node, next_cost))
                elif costlist[next_node] == costlist[node] + next_cost:
                    minload[next_node].append(node)
    return minload


def bfs(d, minload, visit, graph):
    queue = deque([d])
    visit[d] = True
    while queue:
        node = queue.popleft()
        for next_node in minload[node]:
            if visit[next_node] == False:
                queue.append(next_node)
                visit[next_node] = True
            for index in range(len(graph[next_node])):
                if graph[next_node][index][0] == node:
                    graph[next_node][index][1] = -1
    return graph


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for x in range(n)]
    s, d = map(int, input().split())
    for i in range(m):
        u, v, p = map(int, input().split())
        graph[u].append([v, p])
    costlist = [INF for x in range(n)]

    minload = dijkstra(graph, costlist, s)
    visit = [False for _ in range(n)]
    bfs(d, minload, visit, graph)
    costlist = [INF for _ in range(n)]
    dijkstra(graph, costlist, s)

    if costlist[d] == INF:
        print(-1)
    else:
        print(costlist[d])
