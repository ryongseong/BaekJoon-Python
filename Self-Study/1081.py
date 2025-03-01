import sys
input = sys.stdin.readline

def page(N,n):
    c = len(str(N))-1
    a = int(str(N)[0])
    if c == 0:
        if n > a:
            return 0
        else:
            return 1
    result = a*c*10**(c-1) + page(N-a*10**c,n)
    if n > a:
        return result
    if n == a:
        return result + (N-a*10**c+1)
    return result + 10**c

def sumpage(N):
    result = 0
    for n in range(1,10):
        result += page(N,n)*n
    return result

L,U = map(int,input().split())
if L:
    L -= 1
print(sumpage(U)-sumpage(L))