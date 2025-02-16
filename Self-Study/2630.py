import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = []

def sol(x, y, N):
    color = matrix[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != matrix[i][j]:
                sol(x, y, N//2)
                sol(x, y+N//2, N//2)
                sol(x+N//2, y, N//2)
                sol(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

sol(0, 0, N)
print(result.count(0))
print(result.count(1))