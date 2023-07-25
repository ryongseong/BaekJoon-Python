# https://www.acmicpc.net/problem/10773

K = int(input())

game = []
for i in range(K):
    what = int(input())
    if what == 0:
        game.pop()
    else:
        game.append(what)
    
result = sum(game)
print(result)