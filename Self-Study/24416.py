N = int(input())
f = [0] * (N + 2)

cnt = 0


def fibonacci(n):
    global cnt
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


print(fibonacci(N), cnt)
