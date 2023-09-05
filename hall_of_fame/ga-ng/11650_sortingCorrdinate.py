import sys

input = sys.stdin.readline

n = int(input())

cor = [list(map(int, input().split())) for _ in range(n)]
cor.sort()

for i in cor:
    print(i[0], i[1])