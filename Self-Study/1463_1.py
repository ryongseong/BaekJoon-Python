import re


N = int(input())
slogan = input()
rules = re.split(r"[.|:|#]", slogan)
print(sum(int(rule) for rule in rules))
