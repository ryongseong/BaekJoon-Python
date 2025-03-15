import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def sol(arr):
    if len(arr) == 0:
        return

    temp_left, temp_right = [], []
    mid = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mid:
            temp_left = arr[1:i]
            temp_right = arr[i:]
            break
    else:
        temp_left = arr[1:]

    sol(temp_left)
    sol(temp_right)
    print(mid)


pre_order = []

while True:
    try:
        pre_order.append(int(input()))
    except:
        break

sol(pre_order)
