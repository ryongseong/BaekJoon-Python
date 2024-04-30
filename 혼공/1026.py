N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

min_value = 0

A_list.sort(reverse=True)
B_list.sort()

for i in range(N):
    min_value += A_list[i] * B_list[i]

print(min_value)