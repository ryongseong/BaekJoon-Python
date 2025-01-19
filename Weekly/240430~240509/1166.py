# https://www.acmicpc.net/problem/1166

N, L, W, H = map(int, input().split())

left = 0
right = max(L, W, H)

for _ in range(10000):
    mid = (left + right) / 2
    if (L // mid) * (W // mid) * (H // mid) >= N:
        left = mid
    else:
        right = mid

print(left)