import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parents[a] = b
        cnt[b] += cnt[a]


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])
graph.sort()

Q = int(input())
query = []
for _ in range(Q):
    s, e = map(int, input().split())
    query.append([s, e])

low_lst = [0 for _ in range(Q)]
high_lst = [m + 1 for _ in range(Q)]
result = [[0, 0] for _ in range(Q)]

flag = True
while flag:
    query_lists = [[] for _ in range(m + 2)]
    parents = [i for i in range(n + 1)]
    cnt = [1 for _ in range(n + 1)]
    flag = False
    for i in range(Q):
        if low_lst[i] < high_lst[i]:
            mid = (low_lst[i] + high_lst[i]) // 2
            query_lists[mid].append(i)
    for i in range(1, m + 1):
        c, s, e = graph[i - 1]
        union(s, e)
        for j in query_lists[i]:
            flag = True
            root_s = find(query[j][0])
            root_e = find(query[j][1])
            if root_s == root_e:
                high_lst[j] = i
                result[j][0] = c
                result[j][1] = cnt[find(root_s)]
            else:
                low_lst[j] = i + 1

for i in range(Q):
    if low_lst[i] == m + 1:
        print(-1)
    else:
        print(result[i][0], result[i][1])
