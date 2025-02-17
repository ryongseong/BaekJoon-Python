import sys
import heapq
input = sys.stdin.readline


N = int(input())
graph = {}
indegree = {}

for _ in range(N):
    A, B = input().split()
    if A not in indegree:
        indegree[A] = 0
    if B not in indegree:
        indegree[B] = 0
    
    if A not in graph:
        graph[A] = []
    if B not in graph:
        graph[B] = []
    
    graph[A].append(B)
    indegree[B] += 1

queue = []
n_queue = []
result = []
for key, value in indegree.items():
    if value == 0:
        heapq.heappush(queue, key)

while queue:
    value = heapq.heappop(queue)
    result.append(value)

    for n in graph[value]:
        indegree[n] -= 1
        if indegree[n] == 0:
            heapq.heappush(n_queue, n)
    
    if len(queue) == 0:
        queue = n_queue
        n_queue = []

if len(result) != len(indegree):
    print(-1)
else:
    for i in result:
        print(i)