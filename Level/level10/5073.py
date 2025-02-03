def check(a, b, c):
    if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
        return 'Invalid'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    print(check(a, b, c))