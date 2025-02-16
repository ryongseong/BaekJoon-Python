import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.extend(map(int, input().split()))

time = [0 for _ in range(257)]
height = 0
for g in range(257):
    block = B
    for i in matrix:
        if i <= g:
            time[g] += g - i
            block -= g - i
        else:
            time[g] += 2 * (i - g)
            block += i - g
    
    if block >= 0 and time[g] <= time[height]:
        height = g

print(time[height], height)