import sys
sys.setrecursionlimit(10**6)

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cnt = 0
result = -1

def merge(A, p, q, r):
    global cnt, result, K
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    for idx in range(len(tmp)):
        A[p + idx] = tmp[idx]
        cnt += 1
        if cnt == K:
            result = A[p + idx]

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

merge_sort(A, 0, N-1)

print(result)
