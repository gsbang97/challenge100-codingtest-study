n = int(input())

numList = [int(input()) for _ in range(n)]
numList.sort()

for i in range(n):
    print(numList[i])