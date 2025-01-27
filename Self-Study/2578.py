def check(answer):
    for i in range(5):
        if bingo_list[i] == [0, 0, 0, 0, 0]:
            answer += 1
    
    for i in range(5):
        if all(bingo_list[j][i] == 0 for j in range(5)):
            answer += 1
    
    if all(bingo_list[i][i] == 0 for i in range(5)):
        answer += 1
    
    if all(bingo_list[i][4 - i] == 0 for i in range(5)):
        answer += 1
    
    return answer

bingo_list = [list(map(int, input().split())) for _ in range(5)]
call_list = []

for _ in range(5):
    call_list.extend(list(map(int, input().split())))

cnt = 0
answer = 0

for i in range(25):
    for x in range(5):
        for y in range(5):
            if call_list[i] == bingo_list[x][y]:
                bingo_list[x][y] = 0
                cnt += 1
    result = check(answer)
    if result >= 3:
        print(i+1)
        break