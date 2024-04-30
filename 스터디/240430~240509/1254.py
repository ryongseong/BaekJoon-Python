# https://www.acmicpc.net/problem/1254

from collections import deque
import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
for i in range(n):
    if s[i:] == s[i:][::-1]:
        print(n + i)
        break