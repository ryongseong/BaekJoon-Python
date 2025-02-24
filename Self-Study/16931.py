N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

up_side = N * M
left_side = 0
front_side = 0

for r in range(N):
    for c in range(M):
        if c == 0:
            left_side += matrix[r][c]
        else:
            if matrix[r][c-1] < matrix[r][c]:
                left_side += matrix[r][c] - matrix[r][c-1]
        if r == 0:
            front_side += matrix[r][c]
        else:
            if matrix[r-1][c] < matrix[r][c]:
                front_side += matrix[r][c] - matrix[r-1][c]

result = 2 * (up_side + left_side + front_side)

print(result)