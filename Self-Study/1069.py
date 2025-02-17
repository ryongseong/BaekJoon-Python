X, Y, D, T = map(int, input().split())
distance = (X**2 + Y**2) ** 0.5

if distance >= D:
    answer = min(T * (distance//D) + distance % D, T * (distance // D + 1), distance)
else:
    answer = min(T + (D - distance), 2 * T, distance)
print(answer)