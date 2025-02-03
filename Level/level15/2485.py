from math import gcd

N = int(input())

cnt = 0

lst = [int(input()) for _ in range(N)]

diff = []

for i in range(N-1):
    diff.append(lst[i+1] - lst[i])

a = diff[0]
for i in range(1, len(diff)):
    a = gcd(a, diff[i])

for j in diff:
    cnt += j // a - 1

print(cnt)