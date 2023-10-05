# https://www.acmicpc.net/problem/1259

def is_palindrome(number):
    stack = []
    for num in number:
        stack.append(num)
    
    reversed_num = []
    while stack:
        reversed_num.append(stack.pop())

while True:
    N = input()

    if N == '0':
        break

    if is_palindrome(N):
        print("yes")
    else:
        print('no')