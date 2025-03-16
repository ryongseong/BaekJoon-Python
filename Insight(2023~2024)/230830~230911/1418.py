# https://www.acmicpc.net/problem/1418

N = int(input())
K = int(input())

answer_list = [0 for i in range(N+1)]

for i in range(2, N+1):
    if answer_list[i] == 0:
        for j in range(i, N+1, i):
            if j % i == 0:
                answer_list[j] = max(answer_list[j], i)

count = -1
for l in answer_list:
    if l <= K:
        count += 1

print(count)