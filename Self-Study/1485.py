def calculate_line(a, b):
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)

def make_result(lst):
    if len(set(lst)) == 2 and lst.count(max(lst)) == 2 and lst.count(min(lst)) == 4:
        return True
    else:
        return False

T = int(input())

for _ in range(T):
    l = [list(map(int, input().split())) for _ in range(4)]
    l.sort(key=lambda x: (x[0], x[1]))

    answer = [
        calculate_line(l[0], l[1]),
        calculate_line(l[0], l[2]),
        calculate_line(l[0], l[3]),
        calculate_line(l[1], l[2]),
        calculate_line(l[1], l[3]),
        calculate_line(l[2], l[3])
    ]
    
    print(1 if make_result(answer) else 0)