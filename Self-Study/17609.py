import sys

input = sys.stdin.readline


def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def sol(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if is_palindrome_range(s, left + 1, right) or is_palindrome_range(
                s, left, right - 1
            ):
                return 1
            else:
                return 2
    return 0


for _ in range(int(input())):
    print(sol(input().strip()))
