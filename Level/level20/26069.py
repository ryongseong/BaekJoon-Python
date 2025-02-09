import sys
input = sys.stdin.readline

N = int(input())

dance_set = {'ChongChong'}

for _ in range(N):
    a, b = input().split()
    if a in dance_set:
        dance_set.add(b)
    if b in dance_set:
        dance_set.add(a)

print(len(dance_set))