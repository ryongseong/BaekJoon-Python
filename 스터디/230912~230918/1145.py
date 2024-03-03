# # https://www.acmicpc.net/problem/1145

import math

a = list(map(int, input().split()))

answer = []

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            answer.append(math.lcm(a[i], a[j], a[k]))

print(min(answer))