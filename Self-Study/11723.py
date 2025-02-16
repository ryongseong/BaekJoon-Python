import sys
input = sys.stdin.readline

S = set()

def cal(command):
    global S
    if len(command) == 1:
        if command[0] == 'all':
            S = set(i for i in range(1, 21))
        else:
            S = set()
    else:
        c, n = command[0], command[1]
        n = int(n)
        if c == 'add':
            S.add(n)
        elif c == 'remove':
            S.discard(n)
        elif c == 'check':
            print(1 if n in S else 0)
        elif c == 'toggle':
            if n in S:
                S.discard(n)
            else:
                S.add(n)

M = int(input())
for _ in range(M):
    command = input().split()
    cal(command)