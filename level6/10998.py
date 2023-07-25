# https://www.acmicpc.net/problem/10988
import re

def clean_string(string):
    # 구두점 및 공백 제거
    cleaned_string = re.sub('[\W_]', '', string)

    # 소문자로 변환
    cleaned_string = cleaned_string.lower()

    return cleaned_string

def is_palindrome(string):
    cleaned_string = clean_string(string)  # 입력된 문자열 정제

    stack = []  # 빈 스택 생성

    # 정제된 문자열을 스택에 삽입
    for char in cleaned_string:
        stack.append(char)

    reversed_string = ''
    # 스택에서 문자를 제거하면서 뒤집은 문자열 생성
    while stack:
        reversed_string += stack.pop()

    # 정제된 문자열과 뒤집은 문자열을 비교하여 회문 여부 반환
    return cleaned_string == reversed_string

# 사용자로부터 문자열 입력받기
user_input = input()

# 회문인지 여부 출력
if is_palindrome(user_input):
    print(1)
else:
    print(0)