def cutting(start, n):
    if n == 1:
        return
    for i in range(start + n // 3, start + n // 3 * 2):
        result[i] = ' '
    cutting(start, n // 3)
    cutting(start + n // 3 * 2, n // 3)

while True:
    try:
        N = int(input())
        result = ['-'] * (3 ** N)
        cutting(0, 3 ** N)
        print(''.join(result))
    except:
        break