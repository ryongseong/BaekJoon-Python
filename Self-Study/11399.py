N = int(input())

minute_list = list(map(int, input().split()))

minute_list.sort()

result = 0
for idx, minute in enumerate(minute_list):
    result += minute + sum(minute_list[:idx])

print(result)