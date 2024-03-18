# https://www.acmicpc.net/problem/1681 

N, L = map(int, input().split())
L = str(L)

search_num = 0
cnt = 0

while cnt != N:
    search_num += 1
    if L in str(search_num): continue
    cnt += 1

print(search_num)