L = int(input())

height = L * (3 ** 0.5) / 2
width = ((L ** 2) - (height ** 2)) ** 0.5

result = height * width

print(result)