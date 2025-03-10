M = int(input())
result = 1

for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue

    if result == a:
        result = b
    elif result == b:
        result = a

print(result)
