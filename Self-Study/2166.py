N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
matrix.append(matrix[0])

result = 0
for i in range(N):
    result += matrix[i][0] * matrix[i + 1][1] - matrix[i+1][0] * matrix[i][1]

result = abs(result)/ 2
print(round(result, 1))