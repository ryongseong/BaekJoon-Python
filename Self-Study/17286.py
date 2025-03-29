import itertools


def calculate_euclidean_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


yumi_point = list(map(int, input().split()))
person_points = [list(map(int, input().split())) for _ in range(3)]

min_distance = float("inf")

for perm in itertools.permutations(person_points):
    total_distance = 0
    current_point = yumi_point
    for point in perm:
        total_distance += calculate_euclidean_distance(current_point, point)
        current_point = point
    if total_distance < min_distance:
        min_distance = total_distance

print(int(min_distance))
