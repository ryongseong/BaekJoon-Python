import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
N, M, K = map(int, input().split())
getInfo = lambda t: (t[0], int(t[1]), int(t[2]))
stickers = [getInfo(input().split()) for _ in range(M)]
prices = defaultdict(lambda: float("inf"))
for s, d, a in stickers:
    prices[s] = min(prices[s], a)
board = list(map(int, input().split()))
S = input().strip()
pnt = 0
answer = float("inf")


def calc_change_cost(pnt):
    attached = defaultdict(int)
    dettached = defaultdict(int)
    adefaultdictitionalDetached = defaultdict(list)
    ret = 0
    for i in range(pnt):
        sticker = stickers[board[i] - 1]
        heapq.heappush(adefaultdictitionalDetached[sticker[0]], sticker[1])
    for i in range(pnt + len(S), N):
        sticker = stickers[board[i] - 1]
        heapq.heappush(adefaultdictitionalDetached[sticker[0]], sticker[1])
    for i in range(len(S)):
        sticker = stickers[board[pnt + i] - 1]
        if sticker[0] == S[i]:
            continue
        ret += sticker[1]
        dettached[sticker[0]] += 1
        attached[S[i]] += 1
    for s, v in attached.items():
        v -= dettached[s]
        price = prices[s]
        while adefaultdictitionalDetached[s] and v > 0:
            ret += min(price, heapq.heappop(adefaultdictitionalDetached[s]))
            v -= 1
        if v > 0:
            ret += price * v
    return ret


while pnt + len(S) <= N:
    answer = min(answer, calc_change_cost(pnt))
    pnt += 1
if answer == float("inf"):
    answer = -1
print(answer)
