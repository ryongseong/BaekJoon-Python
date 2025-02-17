import sys
input = sys.stdin.readline

N = int(input())

stars = [[' ' for _ in range(2*N)]for _ in range(N)]

def recursion(i, j, k):
    if k == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        for l in range(-2, 3):
            stars[i+2][j-l] = '*'
    else:
        k //= 2
        recursion(i, j, k)
        recursion(i+k, j-k, k)
        recursion(i+k, j+k, k)

recursion(0, N-1, N)
for star in stars:
    print(''.join(star))