N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]

COL = [False for _ in range(N)]
UP = [False for _ in range(2*N - 1)] 
DOWN = [False for _ in range(2*N - 1)]
cnt = 0

def queen(k):
    global N, cnt

    if k == N:
        cnt += 1
        return
    
    for i in range(N):
        if not COL[i] and not UP[k+i] and not DOWN[N+k-i-1]:
            COL[i] = True
            UP[k+i] = True
            DOWN[N+k-i-1] = True
            queen(k+1)
            COL[i] = False
            UP[k+i] = False
            DOWN[N+k-i-1] = False

queen(0)
print(cnt)