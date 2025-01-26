N = int(input())

number_list = list(map(int, input().split()))

result_list = []

for i in range(N):
    if number_list[i] == 0:
        result_list.insert(0, i+1)
    else:
        result_list.insert(number_list[i], i+1)

for i in reversed(result_list):
    print(i, end=' ')