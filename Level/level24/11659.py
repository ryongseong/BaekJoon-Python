import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
l = [0]
t = 0

for i in arr:
    t += i
    l.append(t)

for _ in range(M):
    s, e = map(int, input().split())
    print(l[e] - l[s-1])