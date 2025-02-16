import sys

def f(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    else:
        return int(x)

n = int(sys.stdin.readline().strip())
if n:
    level = []
    for _ in range(n):
        level.append(int(sys.stdin.readline().strip()))

    nn = f(n*0.15)
    level.sort()
    if nn > 0:
        print(f(sum(level[nn:-nn])/len(level[nn:-nn])))
    else:
        print(f(sum(level)/len(level)))
else:
    print(0)