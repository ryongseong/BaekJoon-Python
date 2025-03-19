def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if money_list[a] < money_list[b]:
        parents[b] = a
    else:
        parents[a] = b


N, M, k = map(int, input().split())
parents = [i for i in range(N + 1)]
money_list = [0] + list(map(int, input().split()))

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

friends = set()
cost = 0

for i in range(1, N + 1):
    if find(i) not in friends:
        cost += money_list[parents[i]]
        friends.add(parents[i])

print("Oh no" if cost > k else cost)
