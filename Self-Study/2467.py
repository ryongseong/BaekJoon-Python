import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

result = float("inf")
l, r = 0, 0

for i in range(n - 1):
    current = data[i]

    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + data[mid]

        if abs(tmp) < result:
            result = abs(tmp)
            l = i
            r = mid

            if tmp == 0:
                break

        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1


print(data[l], data[r])
