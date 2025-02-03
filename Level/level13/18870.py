N = int(input())

num_list = list(map(int, input().split()))

sorted_list = sorted(list(set(num_list)))

dic = {sorted_list[i]: i for i in range(len(sorted_list))}

for i in num_list:
    print(dic[i], end=' ')