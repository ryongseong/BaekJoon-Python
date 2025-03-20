import itertools


def valid_permutation(perm, b, p):
    T = [0] * (p + 1)
    for i in range(p):
        T[i + 1] = (T[i] + perm[i]) % p

    f = [0] * p
    for i in range(p + 1):
        for j in range(i + 1, p + 1):
            diff = (T[j] - T[i]) % p
            f[diff] += 1
    return f == b


N, p = int(input().split())
b = list(map(int, input().split()))

if sum(b) != p * (p + 1) // 2:
    print(-1)
    exit()

for perm in itertools.permutations(range(p)):
    if valid_permutation(perm, b, p):
        print(" ".join(map(str, perm)))
        exit()

print(-1)
