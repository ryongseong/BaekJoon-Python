N = int(input())

point_list = []

for _ in range(N):
    point_list.append(tuple(map(int, input().split())))

point_list.sort(key=lambda x: (x[1], x[0]))

for point in point_list:
    print(point[0], point[1])