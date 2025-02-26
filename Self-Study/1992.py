import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]


def sol(N, matrix):
    nums = 0
    for r in matrix:
        nums += sum(r)

    if nums == N**2:
        return "1"
    if nums == 0:
        return "0"

    result = "("
    result += sol(N // 2, [r[: N // 2] for r in matrix[: N // 2]])
    result += sol(N // 2, [r[N // 2 :] for r in matrix[: N // 2]])
    result += sol(N // 2, [r[: N // 2] for r in matrix[N // 2 :]])
    result += sol(N // 2, [r[N // 2 :] for r in matrix[N // 2 :]])
    result += ")"
    return result


print(sol(N, matrix))
