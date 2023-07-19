# https://www.acmicpc.net/problem/10815
N = int(input())
card_list = list(map(int, input().split()))

M = int(input())
cur_list = list(map(int, input().split()))

for i in range(M):
    if cur_list[i] not in card_list:
        print(0, end=" ")
    else:
        print(1, end=" ")