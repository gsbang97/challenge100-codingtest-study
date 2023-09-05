import sys

input = sys.stdin.readline

n = int(input())

lst = []

lst = list(map(int, input().split()))

setlst = sorted(set(lst))
cnt = 0

dic = {setlst[i]: i for i in range(len(setlst))}
for i in lst:
    print(dic[i], end=" ")