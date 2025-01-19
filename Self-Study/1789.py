S = int(input())

N = 1
while (N**2 + N) / 2 <= S:
    N += 1

print(N - 1)