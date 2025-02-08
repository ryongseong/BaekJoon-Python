def is_right_angle(a, b, c):
    return (a ** 2) + (b **2) == (c ** 2)

while True:
    length_list = list(map(int, input().split()))
    if length_list == [0, 0, 0]: break
    print('right' if is_right_angle(*sorted(length_list)) else 'wrong')