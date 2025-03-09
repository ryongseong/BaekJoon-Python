import sys

input = sys.stdin.readline

n = int(input())
m = {}

for i in range(1, n + 1):
    num, str_val, result, me, t, l, length = input().split()
    num, result, me, t, l, length = map(int, [num, result, me, t, l, length])

    if str_val != "megalusion":
        if str_val in m:
            if m[str_val] < 0:
                if result == 4:
                    m[str_val] *= -1
                else:
                    m[str_val] -= 1
        else:
            m[str_val] = 0 if result == 4 else -1

cnt = 0
total_miss = 0

for key, value in m.items():
    if value >= 0:
        cnt += 1
    if value > 0:
        total_miss += value

if cnt == 0:
    print(0)
else:
    avg = (cnt / (cnt + total_miss)) * 100.0
    print(avg)
