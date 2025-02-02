N = int(input())

result = '666'

for _ in range(1, N):
    result = str(int(result) + 1)
    while '666' not in result:
        result = str(int(result) + 1)

print(result)