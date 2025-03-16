# https://www.acmicpc.net/problem/1405

num, E, W, S, N = map(int, input().split())

probabilities = [E/100, W/100, S/100, N/100]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = [[0] * (2*num+1) for _ in range(2*num+1)]

answer = 0

def dfs(x, y, percent, cnt):
    global answer

    if cnt == num:
        answer += percent
        return
    
    now_percent = percent

    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < (2 * num + 1) and 0 <= ny < (2 * num + 1):
            if graph[nx][ny] == 1:
                continue
            else:
                dfs(nx, ny, now_percent * probabilities[i], cnt+1)
                graph[nx][ny] = 0

dfs(num, num, 1, 0)

print(answer)