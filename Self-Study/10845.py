# https://www.acmicpc.net/problem/10845
import sys

input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    command = input().split()

    if 'push' in command:
        arr.append(command[1])
    elif 'pop' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    elif 'size' in command:
        print(len(arr))
    elif 'empty' in command:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif 'back' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])