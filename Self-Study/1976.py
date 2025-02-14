def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
parent = [i for i in range(N+1)]
M = int(input())

for i in range(1, N+1):
    chain = list(map(int, input().split()))
    for j in range(1, N+1):
        if chain[j-1] == 0: continue
        if i == j: continue
        union(i, j)

plan = list(map(int, input().split()))

result = set()
for p in plan:
    result.add(find(p))
    if len(result) != 1:
        print('NO')
        break
else:
    print('YES')