import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split())) # n개의 수를 리스트 안에 넣음

answer = [-1]*n # 정답을 n개의 개수만큼 -1로 초기 설정

stack = []

stack.append(0)
for i in range(1, n):
    while stack and list[stack[-1]] < list[i]: #오른쪽부터 왼쪽으로 계속 크기 비교함
        answer[stack.pop()] = list[i] #결과가 나오면 그 리스트의 수를 뻄
    stack.append(i) #그리고 추가함

print(*answer) #그냥 answer로 했다가 리스트 형태로 나와서 검색해서 찾음 (압축풀기)