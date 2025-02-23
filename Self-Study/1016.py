min_v, max_v = map(int, input().split())

result = max_v - min_v + 1

squares = [False] * result

for i in range(2, int(max_v ** 0.5) + 1):
    square = i ** 2
    for j in range((((min_v-1) // square) + 1) * square, max_v + 1, square):
        if not squares[j - min_v]:
            squares[j - min_v] = True
            result -= 1

print(result)