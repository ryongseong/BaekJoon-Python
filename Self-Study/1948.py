import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
m = int(input())

time = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
cnt = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    back_graph[b].append(a)
    indegree[b] += 1

start, end = map(int, input().split())
queue = deque([start])

while queue:
    x = queue.popleft()
    for i in graph[x]:
        indegree[i[1]] -= 1
        if time[i[1]] < time[x] + i[0]:
            time[i[1]] = time[x] + i[0]
            cnt[i[1]] = [x]
        elif time[i[1]] == time[x] + i[0]:
            cnt[i[1]].append(x)
        
        if indegree[i[1]] == 0:
            queue.append(i[1])

queue = deque([end])
routes = set()
while queue:
    x = queue.popleft()
    for i in cnt[x]:
        if (x, i) not in routes:
            routes.add((x, i))
            queue.append(i)

print(time[end])
print(len(routes))