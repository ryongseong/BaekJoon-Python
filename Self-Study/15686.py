def sol(num, cnt):
    global result
    if num > len(chicken):
        return

    if cnt == M:
        result_tot = 0
        for hx, hy in house:
            min_check = int(1e9)
            for idx in arr:
                cx, cy = chicken[idx]
                min_check = min(min_check, abs(hx - cx) + abs(hy - cy))

            result_tot += min_check

        result = min(result_tot, result)
        return

    arr.append(num)
    sol(num + 1, cnt + 1)
    arr.pop()
    sol(num + 1, cnt)
    return result


N, M = map(int, input().split())
graph = []
house = []
chicken = []
arr = []
INF = int(1e9)
result = INF

for r in range(N):
    graph.append(list(map(int, input().split())))
    for c in range(N):
        if graph[r][c] == 1:
            house.append((r, c))
        elif graph[r][c] == 2:
            chicken.append((r, c))

print(sol(0, 0))
