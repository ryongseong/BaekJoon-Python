for _ in range(int(input())):
    A, B = map(int, input().split())

    while True:
        if A == B:
            print(A * 10)
            break

        if A > B:
            A //= 2
        else:
            B //= 2
