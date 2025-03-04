N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N**2)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for student in students:
    can_sit = []

    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 0:
                prefer, empty = 0, 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if matrix[nr][nc] in student[1:]:
                            prefer += 1

                        if matrix[nr][nc] == 0:
                            empty += 1

                can_sit.append((r, c, prefer, empty))

    can_sit.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    matrix[can_sit[0][0]][can_sit[0][1]] = student[0]

result = 0
satisfaction = [0, 1, 10, 100, 1000]
students.sort()

for r in range(N):
    for c in range(N):
        cnt = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] in students[matrix[r][c] - 1]:
                    cnt += 1

        result += satisfaction[cnt]

print(result)
