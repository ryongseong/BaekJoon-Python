N, M = map(int, input().split())

password = {}

for _ in range(N):
    site, pwd = input().split()
    password[site] = pwd

for _ in range(M):
    site = input()
    print(password[site])