from itertools import product

N, M = map(int, input().split())

perm = product(list(range(1, N+1)), repeat=M)

for p in perm:
    print(*p)