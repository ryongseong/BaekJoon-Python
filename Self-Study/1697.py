N, K = map(int, input().split())

def bfs():
    queue = []
    queue.append(N)
    visited = [0] * 100001
    visited[N] = 1

    while queue:
        x = queue.pop(0)
        if x == K:
            return visited[x] - 1
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

print(bfs())