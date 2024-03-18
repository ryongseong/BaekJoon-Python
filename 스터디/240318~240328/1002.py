# https://www.acmicpc.net/problem/1002 
import math

T = int(input())
answer_list = []

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance == 0:
        if r1 == r2:
            answer_list.append(-1)
        else:
            answer_list.append(0)
    else:
        if (r1 + r2) == distance or abs(r2 - r1) == distance:
            answer_list.append(1)
        elif ((abs(r1 - r2) < distance) and (distance < (r1 + r2))):
            answer_list.append(2)
        else:
            answer_list.append(0)

for answer in answer_list:
    print(answer)