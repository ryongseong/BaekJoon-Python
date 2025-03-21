flag = False
S = input()
E = input()

while E and not flag:
    cur = E[-1]
    E = E[:-1]
    if cur == "B":
        E = E[::-1]
    if S == E:
        flag = True
        break

print(int(flag))
