N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

def solve(idx, first, second):
    if idx == N:
        if len(first) != N//2:
            return -1
        if len(second) != N//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(N//2):
            for j in range(N//2):
                if i == j:
                    continue
                t1 += S[first[i]][first[j]]
                t2 += S[second[i]][second[j]]
        return abs(t1-t2)
    if len(first) > N//2:
        return -1
    if len(second) > N//2:
        return -1
    ans = -1
    t1 = solve(idx+1, first+[idx], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = solve(idx+1, first, second+[idx])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

print(solve(0, [], []))