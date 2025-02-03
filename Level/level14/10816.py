# https://www.acmicpc.net/problem/10816


N = int(input())
given_list = sorted(list(map(int, input().split())))
M = int(input())
compare_list = map(int, input().split())

check_dict = {}

for num in given_list:
    if num in check_dict:
        check_dict[num] += 1
    else:
        check_dict[num] = 1

for num in compare_list:
    if check_dict.get(num) is not None:
        print(check_dict.get(num), end=' ')
    else:
        print(0, end=' ')