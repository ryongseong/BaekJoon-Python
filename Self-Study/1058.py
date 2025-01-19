# https://www.acmicpc.net/problem/1058

N = int(input())

friend_list = []
for _ in range(N):
    friend_list.append(input())

max_friend = 0
for i in range(N):
    friend = 0
    for j in range(N):
        if i == j:
            continue
        if friend_list[i][j] == 'Y':
            friend += 1
        else:
            for k in range(N):
                if friend_list[i][k] == 'Y' and friend_list[k][j] == 'Y':
                    friend += 1
                    break
    max_friend = max(max_friend, friend)

print(max_friend)