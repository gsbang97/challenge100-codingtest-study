import sys
n = int(input())

inputData = sorted(map(int, sys.stdin.readline().rstrip().split()))
ans = 0
nowTime = 0

for i in inputData :
    ans += i + nowTime
    nowTime += i
print(ans)