# https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())

cnt = 0

while True:
    cnt += 1
    if (cnt - E) % 15 == 0 and (cnt - S) % 28 == 0 and (cnt - M) % 19 == 0:
        print(cnt)
        break