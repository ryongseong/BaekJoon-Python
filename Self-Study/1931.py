n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0
for i in range(n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)