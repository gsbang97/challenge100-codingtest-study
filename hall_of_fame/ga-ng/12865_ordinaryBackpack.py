import sys

input = sys.stdin.readline

n, k = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)


for i in range(n):
    w, v = items[i]

    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[-1])