# https://www.acmicpc.net/problem/3003

king, queen, rook, bishop, knight, pawn = 1, 1, 2, 2, 2, 8

k, q, r, b, kn, p = map(int, input().split())

print(king-k, queen-q, rook-r, bishop-b, knight-kn, pawn-p)