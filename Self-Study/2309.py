import sys

height_list = [int(input()) for _ in range(9)]

height_list.sort()
total = sum(height_list)

for i in range(9):
    for j in range(i + 1, 9):
        if total - height_list[i] - height_list[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(height_list[k])
            sys.exit()