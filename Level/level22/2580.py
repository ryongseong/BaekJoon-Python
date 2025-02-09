from collections import deque
import sys
input = sys.stdin.readline

def square_idx(r, c):
    """
    3 x 3 칸의 인덱스 반환
    """
    return (r // 3) * 3 + (c // 3)

def find_next_cell():
    """
    남은 칸 중 가장 가능한 숫자가 적은 칸 선택
    """
    return min(zero_list, key=lambda pos: bin(~(row_mask[pos[0]] | col_mask[pos[1]] | square_mask[square_idx(pos[0], pos[1])]) & 0b1111111110).count('1'))

def make_sudoku():
    if not zero_list:
        for row in matrix:
            print(*row)
        sys.exit(0)
    
    r, c = find_next_cell()
    zero_list.remove((r, c))
    square_index = square_idx(r, c)

    # 가능한 숫자 탐색
    possible_mask = ~(row_mask[r] | col_mask[c] | square_mask[square_index]) & 0b1111111110

    while possible_mask:
        num_bit = possible_mask & -possible_mask # 가장 오른쪽 비트 추출
        num = num_bit.bit_length() - 1 # 1-based index를 맞추기 위해 -1

        # 숫자 배치
        matrix[r][c] = num
        row_mask[r] |= num_bit
        col_mask[c] |= num_bit
        square_mask[square_index] |= num_bit

        # 다음 단계 진행
        make_sudoku()

        # 백트래킹 (숫자 원상복구)
        matrix[r][c] = 0
        row_mask[r] &= ~num_bit
        col_mask[c] &= ~num_bit
        square_mask[square_index] &= ~num_bit

        # 다음 가능한 숫자 확인
        possible_mask &= possible_mask - 1
    
    zero_list.append((r, c)) # 백트래킹 후 다시 빈 칸 리스트에 추가


matrix = [list(map(int, input().split())) for _ in range(9)]

# 숫자 체크용 비트마스크
row_mask = [0] * 9
col_mask = [0] * 9
square_mask = [0] * 9

zero_list = deque()
num_set = set(range(1, 10))

# 스도쿠 초기화 및 비트마스킹 적용
for i in range(9):
    for j in range(9):
        num = matrix[i][j]
        if num == 0:
            zero_list.append((i, j))
        else:
            num_bit = 1 << num
            row_mask[i] |= num_bit
            col_mask[j] |= num_bit
            square_mask[square_idx(i, j)] |= num_bit

make_sudoku()