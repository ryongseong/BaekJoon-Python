import sys

input = sys.stdin.readline


def sol(command):
    if command[0] == "STACK":
        r, c = map(int, command[1:])
        matrix[r][c] += 1
    elif command[0] == "REMOVE":
        r, c = map(int, command[1:])
        if matrix[r][c]:
            matrix[r][c] -= 1
    elif command[0] == "FRONT":
        print(sum(max(row) for row in matrix))
    elif command[0] == "SIDE":
        print(sum(max(matrix[r][c] for r in range(N)) for c in range(M)))
    elif command[0] == "TOP":
        print(sum(1 for r in range(N) for c in range(M) if matrix[r][c]))


N, M, Q = map(int, input().split())

matrix = [[0] * M for _ in range(N)]

for _ in range(Q):
    sol(input().split())
