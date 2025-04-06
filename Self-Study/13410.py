n, k = map(int, input().split())

data = []

for i in range(1, k+1):
    data.append(int(str(n * i)[::-1]))

print(max(data))
