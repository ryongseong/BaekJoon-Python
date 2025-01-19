L, C = map(int, input().split())

word_list = list(input().split())

word_list.sort()

def check(word):
    모음 = 0
    자음 = 0
    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u']:
            모음 += 1
        else:
            자음 += 1
    return 모음 >= 1 and 자음 >= 2

def go(index, selected, word_list):
    if len(selected) == L:
        if check(selected):
            print(selected)
        return
    if index >= len(word_list):
        return
    go(index + 1, selected + word_list[index], word_list)
    go(index + 1, selected, word_list)

go(0, "", word_list)