T = int(input())

def make_result(V, E):
    return 2 - (V - E)

for _ in range(T):
    V, E = map(int, input().split())
    print(make_result(V, E))