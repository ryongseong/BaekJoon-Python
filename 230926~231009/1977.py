# https://www.acmicpc.net/problem/1977
import math

M = int(input())
N = int(input())

answer_list = []

for i in range(M, N+1):
    if math.sqrt(i).is_integer():
        answer_list.append(i)

if len(answer_list)==0:
    print(-1)
else:    
    print(sum(answer_list))
    print(min(answer_list))