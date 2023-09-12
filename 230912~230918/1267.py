N = int(input())
time_list = list(map(int, input().split()))
youngsik = 0
minsik = 0

for time in time_list:
    youngsik += (time//30 + 1) * 10
    minsik   += (time//60 + 1) * 15

if youngsik == minsik:
    print("Y M", minsik)
elif minsik < youngsik:
    print("M", minsik)
else:
    print("Y", youngsik)