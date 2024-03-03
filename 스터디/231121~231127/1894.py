# https://www.acmicpc.net/problem/1894

while True:
    try:
        dot_list = list(map(float,input().split()))

        dot1 = [dot_list[0],dot_list[1]]
        dot2 = [dot_list[2],dot_list[3]]
        dot3 = [dot_list[4],dot_list[5]]
        dot4 = [dot_list[6],dot_list[7]]

        while True:
            if dot2 == dot3:
                break
            dot2,dot1 = dot1,dot2
            if dot2 == dot3:
                break

            dot2,dot1 = dot1,dot2
            dot3,dot4 = dot4,dot3

        tmp = [(dot1[0] + dot4[0])/2,(dot1[1] + dot4[1])/2]

        result = [0.000,0.000]
        for i in range(2):
            if tmp[i] > dot2[i]:
                result[i] = dot2[i] + (tmp[i] - dot2[i]) * 2
            else:
                result[i] = dot2[i] - (dot2[i] - tmp[i]) * 2
        print(f"{result[0]:.3f} {result[1]:.3f}")
    except:
        break