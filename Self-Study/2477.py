K = int(input())

width = []
height = []
all_area = []

for _ in range(6):
    dir, length = map(int, input().split())

    if dir == 1 or dir == 2:
        width.append(length)
        all_area.append(length)
    else:
        height.append(length)
        all_area.append(length)

board = max(width) * max(height)

max_height_idx = all_area.index(max(height))
max_width_idx = all_area.index(max(width))

minus_area_1 = abs(all_area[max_height_idx - 1] - all_area[(max_height_idx - 5) if max_height_idx == 5 else max_height_idx + 1])
minus_area_2 = abs(all_area[max_width_idx - 1] - all_area[(max_width_idx - 5) if max_width_idx == 5 else max_width_idx + 1])

print(K * (board - (minus_area_1 * minus_area_2)))