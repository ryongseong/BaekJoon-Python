N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if matrix[j][i] and matrix[i][k]:
                matrix[j][k] = 1

for a in matrix:
    print(*a)
