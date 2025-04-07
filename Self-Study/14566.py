n = int(input())
data = list(map(int, input().split()))
cnt = 0
min_value = float("inf")

for i in range(n - 1):
    for j in range(i + 1, n):
        value = abs(data[i] - data[j])
        if min_value > value:
            min_value = value
            cnt = 1
        elif min_value == value:
            cnt += 1

print(min_value, cnt)
