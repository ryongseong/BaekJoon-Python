import sys


stack1 = list(sys.stdin.readline().rstrip())
#stack1에 문자열을 입력받아 불필요한 공백을 지우고 저장한다.
stack2 = []
#cursor을 대신해 빈 리스트를 생성한다.

for _ in range(int(input())): #숫자를 입력해 그 수만큼의 커맨드를 입력받음
    command = sys.stdin.readline().split() #커맨드를 리스트형태로 입력받음.
    if command[0] == "L" and stack1: 
        #커맨드의 0번 인덱스가 L이면서 stack1이 비어있지 않다면
        stack2.append(stack1.pop())
        #stack1에서 가장 뒤의 값을 빼서 stack2의 맨 뒤에 추가함.
    elif command[0] == "D" and stack2:
        #커맨드의 0번 인덱스가 D이면서 stack2가 비어있지 않다면
        stack1.append(stack2.pop())
        #stack2에서 가장 뒤의 값을 빼서 stack1의 맨 뒤에 추가함.
    elif command[0] == "B" and stack1:
        #커맨드의 0번 인덱스가 B이면서 stack1이 비어있지 않다면
        stack1.pop()
        #stack1의 맨 뒤에 있는 값을 뺌(삭제)
    elif command[0] == "P":
        #커맨드의 0번 인덱스가 P이면
        stack1.append(command[1])
        #커맨드의 1번 인덱스의 값을 stack1의 맨 뒤에 추가함.

print(''.join(stack1+list(reversed(stack2))))
#stack1의 뒤에 stack2를 뒤집은 값을 리스트 형태로 만들어 결합한 뒤 리스트 형태를 하나의 문자로 연결한다.