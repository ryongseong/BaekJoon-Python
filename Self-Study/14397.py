import sys

count = int(0)
n, m = map(int, sys.stdin.readline().split())
stack = []
for i in range(0, n):
    a = list(map(str, sys.stdin.readline()))
    a.pop()
    stack.append(a)

for i in range(0, n):
    for t in range(0, m - 1):
        if (stack[i][t] == "." and stack[i][t + 1] == "#") or (
            stack[i][t] == "#" and stack[i][t + 1] == "."
        ):
            count += 1

for i in range(0, n - 1):
    if i % 2 == 0:
        if (stack[i][0] == "." and stack[i + 1][0] == "#") or (
            stack[i][0] == "#" and stack[i + 1][0] == "."
        ):
            count += 1
        for t in range(1, m):
            if (stack[i][t] == "." and stack[i + 1][t] == "#") or (
                stack[i][t] == "#" and stack[i + 1][t] == "."
            ):
                count += 1
            if (stack[i][t] == "." and stack[i + 1][t - 1] == "#") or (
                stack[i][t] == "#" and stack[i + 1][t - 1] == "."
            ):
                count += 1
    else:
        for t in range(0, m - 1):
            if (stack[i][t] == "." and stack[i + 1][t] == "#") or (
                stack[i][t] == "#" and stack[i + 1][t] == "."
            ):
                count += 1
            if (stack[i][t] == "." and stack[i + 1][t + 1] == "#") or (
                stack[i][t] == "#" and stack[i + 1][t + 1] == "."
            ):
                count += 1
        if (stack[i][m - 1] == "." and stack[i + 1][m - 1] == "#") or (
            stack[i][m - 1] == "#" and stack[i + 1][m - 1] == "."
        ):
            count += 1

print(count)
