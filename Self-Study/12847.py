n, m = map(int, input().split())

datas = list(map(int, input().split()))

result = current = sum(datas[:m])

for i in range(n - m):
    current += datas[m + i] - datas[i]
    result = max(result, current)

print(result)
