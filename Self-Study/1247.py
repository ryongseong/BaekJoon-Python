for _ in range(3):
    N = int(input())
    data = [int(input()) for _ in range(N)]

    if sum(data) == 0:
        print("0")
    elif sum(data) > 0:
        print("+")
    else:
        print("-")
