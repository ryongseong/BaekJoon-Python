# https://www.acmicpc.net/problem/1076

input_list = []

for _ in range(3):
    input_list.append(input())

value_list = input_list[:2]
multiplier_value = input_list[-1];

resistance_dict = {
    'black' : ['0', 1],
    'brown' : ['1', 10],
    'red': ['2', 100],
    'orange': ['3', 1000],
    'yellow': ['4', 10000],
    'green': ['5', 100000],
    'blue': ['6', 1000000],
    'violet': ['7', 10000000],
    'grey': ['8', 100000000],
    'white': ['9', 1000000000]
}

print(int(resistance_dict[value_list[0]][0] + resistance_dict[value_list[1]][0]) * resistance_dict[multiplier_value][1])