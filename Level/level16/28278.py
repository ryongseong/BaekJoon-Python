import sys
input = sys.stdin.readline
N = int(input())

lst = []

def get_result(command):
    global lst
    if command[0] == 2:
        print(-1 if len(lst) == 0 else lst.pop())
    elif command[0] == 3:
        print(len(lst))
    elif command[0] == 4:
        print(1 if len(lst) == 0 else 0)
    elif command[0] == 5:
        print(-1 if len(lst) == 0 else lst[-1])

def append_list(command):
    global lst
    lst.append(command[1])

for _ in range(N):
    command = list(map(int, input().split()))
    if command[0] == 1:
        append_list(command)
    else:
        get_result(command)