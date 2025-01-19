# https://www.acmicpc.net/problem/10866
import sys

input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    command = input().split()
    if 'push_front' in command:
        arr.insert(0, int(command[-1]))
    elif 'push_back' in command:
        arr.append(int(command[-1]))
    elif 'pop_front' in command:
        if len(arr) == 0:
            print(-1)
        else: print(arr.pop(0))
    elif 'pop_back' in command:
        if len(arr) == 0:
            print(-1)
        else: print(arr.pop(-1))
    elif 'size' in command:
        print(len(arr))
    elif 'empty' in command:
        if len(arr) == 0:
            print(1)
        else: print(0)
    elif 'front' in command:
        if len(arr) == 0:
            print(-1)
        else:print(int(arr[0]))
    elif 'back' in command:
        if len(arr) == 0:
            print(-1)
        else:print(arr[-1])