# https://www.acmicpc.net/problem/1759
def jamo_check(answer):
    mo = []
    ja = []
    for a in answer:
        if a in "aeiou":
            mo.append(a)
        else: ja.append(a)
    return bool(mo and len(ja) >= 2)


def dfs(idx, depth):
    if depth == L and jamo_check(answer):
        print(''.join(answer))
        return
    for i in range(idx, C):
        answer.append(dict[i])
        dfs(i+1, depth+1)
        answer.pop(-1)

L, C = map(int, input().split(" "))
dict = input().split(" ")
dict.sort()

answer = []
dfs(0,0)
