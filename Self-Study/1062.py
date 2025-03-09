import sys

input = sys.stdin.readline

N, K = map(int, input().split())

words = []
for _ in range(N):
    bitmask = 0
    for c in set(input().strip()):
        bitmask |= 1 << (ord(c) - ord("a"))
    words.append(bitmask)

if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

learn_alpha = 0
for c in ("a", "c", "i", "n", "t"):
    learn_alpha |= 1 << (ord(c) - ord("a"))

result = 0


def dfs(idx, cnt, learn_alpha):
    global result

    if cnt == K - 5:
        read_cnt = sum(1 for word in words if word & ~learn_alpha == 0)
        result = max(result, read_cnt)
        return

    for i in range(idx, 26):
        if not (learn_alpha & (1 << i)):
            dfs(i + 1, cnt + 1, learn_alpha | (1 << i))


dfs(0, 0, learn_alpha)
print(result)
