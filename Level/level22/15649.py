# https://www.acmicpc.net/problem/15649

N, M = list(map(int, input().split()))

def f(s):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1):
        if i in s:
            continue
        f(s + [i])

f([])