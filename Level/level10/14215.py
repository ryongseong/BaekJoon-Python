a, b, c = map(int, input().split())

while True:
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if a + b > c:
        break
    c -= 1

print(sum((a, b, c)))