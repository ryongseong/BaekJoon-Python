def sol(x, y, w):
    a = (x ** 2 - w ** 2) ** 0.5
    b = (y ** 2 - w ** 2) ** 0.5
    return a * b / (a + b)

x, y, c = map(float, input().split())
start, end = 0, min(x, y)
result = 0

while (end - start) > 0.000001:
    w = (start + end) / 2
    result = w
    if sol(x, y, w) >= c:
        start = w
    else:
        end = w

print(result)