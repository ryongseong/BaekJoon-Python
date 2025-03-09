T = 0

while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break

    a = V // P
    b = V % P

    if b > L:
        b = L

    result = a * L + b

    T += 1
    print(f"Case {T}: {result}")
