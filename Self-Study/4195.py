def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])


for _ in range(int(input())):
    F = int(input())
    parent, number = {}, {}
    for _ in range(F):
        a, b = input().split()
        if parent.get(a) is None:
            parent[a] = a
            number[a] = 1
        if parent.get(b) is None:
            parent[b] = b
            number[b] = 1
        union(a, b)