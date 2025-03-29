N, D, K = map(int, input().split())
s = list(map(int, input().split()))
dots = [0] * N
cnt = 0

for _ in range(D):
    for i in range(N):
        dots[i] += s[i]

    if any(star > K for star in dots):
        cnt += 1
        dots = s[:]

print(cnt)
