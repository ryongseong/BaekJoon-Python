# https://www.acmicpc.net/problem/3009

x_dot_list = []
y_dot_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_dot_list.append(x)
    y_dot_list.append(y)

for i in range(3):
    if x_dot_list.count(x_dot_list[i]) == 1:
        x4 = x_dot_list[i]
    if y_dot_list.count(y_dot_list[i]) == 1:
        y4 = y_dot_list[i]

print(x4, y4)