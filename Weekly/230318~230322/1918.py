import sys
input = sys.stdin.readline

def prefix(fix):        # 후위 표기식에 대한 식을 정의
    stack = list()      # 스택이라는 변수를 리스트 형태로 정의

    for i in range(len(fix) - 1): 
        if (fix[i] == "("):
            stack.append(fix[i])
        elif (fix[i] == "+" or fix[i] == "-"): # i번째가 +나 - 이면서
            while(stack and stack[-1] != "("): #i번째나 i 앞번째가 (가 아닐때
                print(stack.pop(), end = "") # 스택에서 꺼낸다.
            stack.append(fix[i]) # i번째나 i 앞번째가 (일 경우에는 스택에 추가한다.
        elif (fix[i] == "*" or fix[i] == "/"): # i번째가 *나 / 이면서
            while (stack and stack[-1] != '(' and (stack[-1] == "*" or stack[-1] =='/')): # i 앞번째가 (가 아니면서 *나 /가 아닐때
                print(stack.pop(), end="") # i번째 값을 스택에서 꺼낸다.
            stack.append(fix[i]) 
        elif (fix[i] == ")"): # i번째 값이 (일 경우
            while (stack and stack[-1] != '('): # i 앞번째가 (이 아닐때
                print(stack.pop(), end="") #값을 꺼낸다.
            stack.pop()
        elif (fix[i] >= 'A' and fix[i] <= 'Z'): #알파벳일 경우 바로 출력
            print(fix[i], end="")

    if (len(stack) > 0): # 스택에 아무것도 없을 때까지 계속해서 값을 꺼냄
        for i in range(len(stack)):
            print(stack.pop(), end="")


fix = sys.stdin.readline()
prefix(fix)