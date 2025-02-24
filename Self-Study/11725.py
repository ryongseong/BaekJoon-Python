N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N+1)]
stack = [1]

while stack:
    cur = stack.pop()
    for i in graph[cur]:
        if visited[i] == 0:
            visited[i] = cur
            stack.append(i)

for i in range(2, N+1):
    print(visited[i])