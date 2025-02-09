def is_boxing(num, W, H):
    if num <= ((W**2) + (H**2)) ** 0.5:
        return 'DA'
    else:
        return 'NE'


N, W, H = map(int, input().split())
for _ in range(N):
    print(is_boxing(int(input()), W, H))