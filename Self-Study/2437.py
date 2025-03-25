import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))

result = 1
for num in arr:
    if result < num:
        break
    result += num
print(result)
