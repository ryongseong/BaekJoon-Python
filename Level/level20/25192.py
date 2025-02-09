import sys
input = sys.stdin.readline

N = int(input())
chat_lst = set()
cnt = 0

for _ in range(N):
    user = input().strip()
    if user == 'ENTER':
        cnt += len(chat_lst)
        chat_lst.clear()
    else:
        chat_lst.add(user)

cnt += len(chat_lst)
print(cnt)