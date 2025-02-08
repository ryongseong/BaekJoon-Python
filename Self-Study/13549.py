from collections import deque

def bfs(N, K):
    queue = deque([N])
    visited[N] = 1

    while queue:
        x = queue.popleft()
        if x == K:
            return
        for i in (2*x, x-1, x+1):
            if i < 0 or i > 100000:
                continue
            if visited[i]:
                continue

            if i == 2 * x:
                visited[i] = visited[x]
            else:
                visited[i] = visited[x] + 1
            
            queue.append(i)

N, K = map(int, input().split())
visited = [0] * 100001
bfs(N, K)
print(visited[K] - 1)