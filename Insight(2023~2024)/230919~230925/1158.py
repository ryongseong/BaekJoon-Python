# https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]

answer = []
count = 0

for j in range(N):
    count += K-1
    if count >= len(lst):
        count %= len(lst)
    
    answer.append(str(lst.pop(count)))

print("<", ", ".join(answer)[:],">", sep="")