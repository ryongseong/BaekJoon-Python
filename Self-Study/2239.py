def row_check(r, num):
    for x in range(9):
        if num == sudoku[r][x]:
            return False
    return True


def col_check(c, num):
    for x in range(9):
        if num == sudoku[x][c]:
            return False
    return True


def three_check(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if sudoku[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth):
    if depth >= len(target):
        for k in range(9):
            print(''.join(map(str, sudoku[k])))
        exit()

    nr, nc = target[depth]
    for j in range(1, 10):
        if row_check(nr, j) and col_check(nc, j) and three_check(nr, nc, j):
            sudoku[nr][nc] = j
            dfs(depth + 1)
            sudoku[nr][nc] = 0


sudoku = []
target = []
for i in range(9):
    temp = list(map(int, input()))
    for j in range(len(temp)):
        if temp[j] == 0:
            target.append((i, j))
    sudoku.append(temp)

dfs(0)