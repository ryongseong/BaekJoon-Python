# https://www.acmicpc.net/problem/10815

N = int(input())
card_list = sorted(list(map(int,input().split())))
M = int(input())
cur_list = map(int, input().split())

for card in cur_list:
    low, high = 0, N-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if card_list[mid] > card:
            high = mid - 1
        elif card_list[mid] < card:
            low = mid + 1
        else:
            exist = True
            break
    
    print(1 if exist else 0, end=' ')