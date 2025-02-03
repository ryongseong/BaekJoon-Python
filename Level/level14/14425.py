N, M = map(int, input().split())

S = {input().strip() for _ in range(N)}

cnt = 0
for _ in range(M):
    if input().strip() in S:
        cnt += 1

print(cnt)
