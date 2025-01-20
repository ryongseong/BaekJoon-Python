N = int(input())

checker_list = [list(map(int, input().split())) for _ in range(N)]

result = [float('inf')] * N

for x in checker_list:
    for y in checker_list:
        distance = []
        for dx, dy in checker_list:
            distance.append(abs(x[0] - dx) + abs(y[1] - dy))
        
        distance.sort()
        cnt = 0
        for i in range(N):
            cnt += distance[i]
            result[i] = min(result[i], cnt)

print(*result)