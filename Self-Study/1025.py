N, M = map(int, input().split())

num_list = [input() for _ in range(N)]

answer = -1

def sqrt(S):
    S = int(S)
    return int(S ** 0.5) ** 2 == S

for i in range(N):
    for j in range(M):
        for row_d in range(-N, N):
            for col_d in range(-M, M):
                S = ""
                x, y = i, j
                if row_d == 0 and col_d == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    S += num_list[x][y]
                    if sqrt(S):
                        answer = max(answer, int(S))
                    x += row_d
                    y += col_d
print(answer)