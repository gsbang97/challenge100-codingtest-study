import sys

input = sys.stdin.readline

n = int(input())

lst = [input().rstrip() for _ in range(n)]
lst = sorted(set(lst))
lst.sort(key = len)


for i in lst:
    print(i)