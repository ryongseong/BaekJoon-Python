N = int(input())
arr = list(map(int, input().split()))

inc = 1
length = 1

for i in range(1, N):
    if arr[i] >= arr[i-1]:
        inc += 1
    else:
        inc = 1
    length = max(length, inc)

dec = 1
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        dec += 1
    else:
        dec = 1
    length = max(length, dec)

print(length)