# https://www.acmicpc.net/problem/1085

# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int,input().split())

left = (0, 0)
now = (x, y)
right = (w, h)

now_left = [a - b for a, b in zip(now, left)]
now_right = [a - b for a, b in zip(right, now)]

print(min(min(now_left), min(now_right)))