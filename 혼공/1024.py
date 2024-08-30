# https://www.acmicpc.net/problem/1024

import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for l in range(L, 101):
    if (2*N + l - l**2) % (2*l) == 0 and (2*N + l - l**2) // (2*l) >= 0:
        start = (2*N + l - l**2) // (2*l)
        for i in range(l):
            print(start + i, end=' ')
        exit()
print(-1)