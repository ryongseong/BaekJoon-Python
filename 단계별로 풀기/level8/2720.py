# https://www.acmicpc.net/problem/2720

T = int(input())

for _ in range(T):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i
	print()