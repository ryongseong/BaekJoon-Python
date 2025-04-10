dic = {
    "SONGDO": "HIGHSCHOOL",
    "CODE": "MASTER",
    "2023": "0611",
    "ALGORITHM": "CONTEST",
}


n = input()

if dic.get(n) is not None:
    print(dic[n])
