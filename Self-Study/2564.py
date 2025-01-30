width, height = map(int, input().split())
store_num = int(input())
stores = [list(map(int, input().split())) for _ in range(store_num)]
dong = list(map(int, input().split()))

def calculate_distance(dir, dist):
    if dir == 1: return dist
    elif dir == 2: return 2 * width + height - dist
    elif dir == 3: return 2 * (width + height) - dist
    else: return width + dist

total_distance = 2 * (width + height)
start_distance = calculate_distance(dong[0], dong[1])
result = 0

for store in stores:
    store_distance = calculate_distance(store[0], store[1])

    dist1 = abs(start_distance - store_distance)
    dist2 = total_distance - dist1

    result += min(dist1, dist2)

print(result)