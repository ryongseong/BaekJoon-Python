# https://www.acmicpc.net/problem/2738

N, M = map(int,input().split())

matrix_A=[]
matrix_B=[]

for _ in range(N):
    matrix_A.append(list(map(int, input().split())))
for _ in range(N):
    matrix_B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(matrix_A[i][j] + matrix_B[i][j], end=' ')
    print()