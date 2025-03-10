while True:
    N = input()
    if N == "0":
        break
    result = 1
    for i in N:
        result += 1
        if i == "1":
            result += 2
        elif i == "0":
            result += 4
        else:
            result += 3

    print(result)
