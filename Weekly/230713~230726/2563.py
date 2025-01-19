# 색종이의 개수 입력.
paper = int(input())

# 보드를 100x100 크기로 만듦.
board = [[0] * 100 for a in range(100)]

# 색종이 최종 넓이 초깃값 0 할당.
result = 0

# 색종이의 개수만큼
for a in range(paper):
# 좌표 입력.
    x, y = map(int, input().split())

# 가로 길이가 10이라고 나와있음.
    for i in range(x, x+10):
# 세로 길이가 10이라고 나와있음.
        for j in range(y, y+10):
# 보드에 색종이 붙이기
            board[i][j] = 1

# 가로가 100
for i in range(100):
# 세로가 100
    for j in range(100):
# 만약 색종이가 붙어져 있다면, 겹치는 부분 무시
        if board[i][j] == 1:
# 넓이 1 추가
            result += 1

# 결과 출력
print(result)