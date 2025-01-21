from collections import deque

def right(idx, d):
    if idx > 3:
        return
    if wheel_list[idx - 1][2] != wheel_list[idx][6]:
        right(idx + 1, -d)
        wheel_list[idx].rotate(d)

def left(idx, d):
    if idx < 0:
        return
    if wheel_list[idx][2] != wheel_list[idx + 1][6]:
        left(idx - 1, -d)
        wheel_list[idx].rotate(d)

wheel_list = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    idx, d = map(int, input().split())
    idx -= 1
    left(idx - 1, -d)
    right(idx + 1, -d)
    wheel_list[idx].rotate(d)

score = 0
for i in range(4):
    if wheel_list[i][0] == 1:
        score += 2 ** i

print(score)