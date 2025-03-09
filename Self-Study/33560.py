def save_result(current_score):
    if current_score < 35:
        return 0
    if current_score < 65:
        return 1
    if current_score < 95:
        return 2
    if current_score < 125:
        return 3
    return 4


def reset_game():
    global current_score, current_time, get_score, get_time
    current_score, current_time, get_score, get_time = 0, 0, 1, 4


n = int(input())
dices = list(map(int, input().split()))

current_score, current_time, get_score, get_time = 0, 0, 1, 4

result = [0] * 5

a = 0
while True:
    if a == n:
        break
    if current_time > 240:
        result[save_result(current_score)] += 1
        reset_game()
    dice = dices[a]

    if dice == 1:
        result[save_result(current_score)] += 1
        reset_game()
        a += 1
        continue
    elif dice == 2:
        if get_score > 1:
            get_score /= 2
        elif get_score == 1:
            get_time += 2
    elif dice == 4:
        current_time += 56
    elif dice == 5:
        if get_time > 1:
            get_time -= 1
    elif dice == 6:
        if get_score < 32:
            get_score *= 2

    current_time += get_time
    current_score += get_score
    a += 1


for i in range(1, 5):
    print(result[i])
