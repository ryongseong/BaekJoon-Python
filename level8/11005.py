# https://www.acmicpc.net/problem/11005

import string

N, B = map(int, input().split())
tmp = string.digits+string.ascii_uppercase

def convert(N, B):
    q, r = divmod(N, B)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, B) + tmp[r]
    
print(convert(N, B))