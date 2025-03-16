for _ in range(int(input())):
    N = int(input())
    parent = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    a, b = map(int, input().split())
    parents_a, parents_b = [0, a], [0, b]

    while parent[a]:
        parents_a.append(parent[a])
        a = parent[a]
    while parent[b]:
        parents_b.append(parent[b])
        b = parent[b]

    i = -1
    while parents_a[i] == parents_b[i]:
        i -= 1

    print(parents_a[i + 1])
