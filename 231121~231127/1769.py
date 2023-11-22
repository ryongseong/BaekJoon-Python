# https://www.acmicpc.net/problem/1769 

X = input()

cnt = 0
while int(X) >= 10:
    Y = 0
    for i in range(len(X)):
        Y += int(X[i])
    cnt += 1
    X = str(Y)

print(cnt)
print("YES" if int(X)%3 == 0 else "NO")