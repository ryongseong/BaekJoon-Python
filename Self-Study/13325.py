import sys

input = sys.stdin.readline

k = int(input())
node_cnt = 2 ** (k + 1)
weights = [0] + list(map(int, input().split()))
result = sum(weights)

left = node_cnt // 2 - 1
right = node_cnt - 1

while right:
    for i in range((right - left) // 2):
        c = left + (2 * i)
        n = c // 2

        weights[n] += max(weights[c], weights[c + 1])
        result += abs(weights[c] - weights[c + 1])

    right = left
    left //= 2

print(result)
