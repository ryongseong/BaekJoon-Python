while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = 1
    for i in range(arr[0]):
        n = n * arr[2 * i + 1] - arr[2 * i + 2]

    print(n)
