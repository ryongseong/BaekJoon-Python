# https://www.acmicpc.net/problem/1138 

N = int(input())

tall_list = list(map(int, input().split()))
answer = [0] * N

for i in range(N):   
    cnt = 0
    for j in range(N):
        if cnt == tall_list[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1

for i in answer:
    print(i, end=' ')