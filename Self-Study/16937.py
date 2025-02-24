H, W = map(int, input().split())
N = int(input())

stickers = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(i+1, N):
        R1, C1 = stickers[i]
        R2, C2 = stickers[j]

        if (R1 + R2 <= H and max(C1, C2) <= W) or (max(R1, R2) <= H and C1 + C2 <= W):
            answer = max(answer, R1 * C1 + R2 * C2)
        if (C1 + R2 <= H and max(R1, C2) <= W) or (max(C1, R2) <= H and R1 + C2 <= W):
            answer = max(answer, R1 * C1 + R2 * C2)
        if (C1 + C2 <= H and max(R1, R2) <= W) or (max(C1, C2) <= H and R1 + R2 <= W):
            answer = max(answer, R1 * C1 + R2 * C2)
        if (R1 + C2 <= H and max(C1, R2) <= W) or (max(R1, C2) <= H and C1 + R2 <= W):
            answer = max(answer, R1 * C1 + R2 * C2)

print(answer)