# https://www.acmicpc.net/problem/1004

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5
        d2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5

        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            count += 1

    print(count)