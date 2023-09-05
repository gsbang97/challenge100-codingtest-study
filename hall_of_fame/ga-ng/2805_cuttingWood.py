import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)
res = 0

while start <= end:
    h = (end + start) // 2

    total = sum(x - h for x in trees if x > h)
    if total < m:
        end = h - 1
    else:
        res = h
        start = h + 1

print(res)