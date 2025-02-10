N = int(input())

A = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = float('-inf')
min_value = float('inf')

def dfs(i, result, add, sub, mul, div):
    global max_value, min_value
    if i == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    if add:
        dfs(i+1, result+A[i], add-1, sub, mul, div)
    if sub:
        dfs(i+1, result-A[i], add, sub-1, mul, div)
    if mul:
        dfs(i+1, result*A[i], add, sub, mul-1, div)
    if div:
        dfs(i+1, int(result/A[i]), add, sub, mul, div-1)

dfs(1, A[0], *operators)
print(max_value)
print(min_value)
