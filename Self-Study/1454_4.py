import math
import heapq

N = int(input().strip())

if N == 0:
    print("0 0")
    exit()
if N == 1:
    print("1 1")
    exit()

heap = []
heapq.heappush(heap, (0, 0, N))
best = {N: (0, 0)}

while heap:
    days, water, x = heapq.heappop(heap)
    if best.get(x, (float("inf"), float("inf"))) < (days, water):
        continue

    if x == 1:
        print(days + 1, water + 1)
        break

    if x - 1 >= 1:
        nx = x - 1
        ndays = days + 1
        nwater = water + 1
        if nx not in best or (ndays, nwater) < best[nx]:
            best[nx] = (ndays, nwater)
            heapq.heappush(heap, (ndays, nwater, nx))

    if x % 3 == 0:
        nx = x // 3
        if nx >= 1:
            ndays = days + 1
            nwater = water + 3
            if nx not in best or (ndays, nwater) < best[nx]:
                best[nx] = (ndays, nwater)
                heapq.heappush(heap, (ndays, nwater, nx))

    sqrt_x = math.isqrt(x)
    if sqrt_x * sqrt_x == x and sqrt_x >= 1:
        nx = sqrt_x
        ndays = days + 1
        nwater = water + 5
        if nx not in best or (ndays, nwater) < best[nx]:
            best[nx] = (ndays, nwater)
            heapq.heappush(heap, (ndays, nwater, nx))
