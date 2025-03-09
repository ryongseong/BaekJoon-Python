import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = sorted([list(map(int, input().split())) for _ in range(N)])

    top = 0
    answer = 1

    for i in range(1, N):
        if scores[i][1] < scores[top][1]:
            top = i
            answer += 1

    print(answer)
