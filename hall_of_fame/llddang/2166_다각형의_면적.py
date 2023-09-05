import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
area = 0
for i in range(N):
    area += arr[i][0] * arr[0][1] if (i == N-1) else arr[i][0] * arr[i+1][1]
    area -= arr[i][0] * arr[N-1][1] if (i == 0) else arr[i][0] * arr[i-1][1]
print(abs(area) / 2)
