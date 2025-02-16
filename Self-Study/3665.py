import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]

    T = list(map(int, input().split()))

    lose = [i for i in range(1, N+1)]
    for w in T:
        lose.remove(w)
        for l in lose:
            graph[w].append(l)
            indegree[l] += 1
    
    M = int(input())
    for _ in range(M):
        A, B = map(int, input().split())
        if B in graph[A]:
            graph[A].remove(B)
            graph[B].append(A)
            indegree[A] += 1
            indegree[B] -= 1
        else:
            graph[B].remove(A)
            graph[A].append(B)
            indegree[A] -= 1
            indegree[B] += 1
    
    queue = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    answer = []
    while queue:
        temp = queue.popleft()
        answer.append(temp)
        for i in graph[temp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    if any(indegree):
        print("IMPOSSIBLE")
    else:
        print(*answer)