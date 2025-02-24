T = int(input())

for _ in range(T):
    N = int(input())
    A_stickers = list(map(int, input().split()))
    B_stickers = list(map(int, input().split()))
    if N == 1:
        print(max(A_stickers[0], B_stickers[0]))
        continue

    A_stickers[1] += B_stickers[0]
    B_stickers[1] += A_stickers[0]

    for i in range(2, N):
        A_stickers[i] += max(B_stickers[i-1], B_stickers[i-2])
        B_stickers[i] += max(A_stickers[i-1], A_stickers[i-2])
    
    print(max(A_stickers[N-1], B_stickers[N-1]))