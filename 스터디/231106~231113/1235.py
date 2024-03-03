# https://www.acmicpc.net/problem/1235

num = int(input())

num_list = []

for _ in range(num):
    num_list.append(input())

for i in range(1, len(num_list[0])+1):
    results = []
    for j in range(num):
        if num_list[j][-i:] in results:
            break
        else:
            results.append(num_list[j][-i:])
    if len(results)==num:
        print(i)
        break