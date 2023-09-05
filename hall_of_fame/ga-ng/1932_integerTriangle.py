import sys

input = sys.stdin.readline

n = int(input())

dp = [list(map(int, input().split())) for _ in range(n)]
dp.reverse()
# print(dp)

for k in range(1, len(dp)):
    for j in range(0, len(dp[k])):

        dp[k][j] += max(dp[k-1][j], dp[k-1][j+1])


print(dp[-1][-1])