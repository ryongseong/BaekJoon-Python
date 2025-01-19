# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def z(N, r, c):
    if N == 0:
        return 0
    cur_count = 2 * (r % 2) + (c % 2)
    return 4 * z(N - 1, r // 2, c // 2) + cur_count

print(z(N, r, c))