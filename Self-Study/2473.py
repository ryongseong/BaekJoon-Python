import sys

input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))

result = float("inf")
l, m, r = 0, 0, 0

for i in range(n - 2):
    if i > 0 and data[i] == data[i - 1]:
        continue

    start, end = i + 1, n - 1

    while start < end:
        tmp = data[i] + data[start] + data[end]

        if abs(tmp) < result:
            result = abs(tmp)
            l, m, r = i, start, end

        if tmp < 0:
            start += 1
            while start < end and data[start] == data[start - 1]:
                start += 1
        elif tmp > 0:
            end -= 1
            while start < end and data[end] == data[end + 1]:
                end -= 1
        else:
            print(data[l], data[m], data[r])
            sys.exit(0)

print(data[l], data[m], data[r])
