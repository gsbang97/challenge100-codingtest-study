import sys

input = sys.stdin.readline

n = int(input())    ## nxn 배열이 존재 할 때


k = int(input())    ## 1차원 배열에서 k 번째에 있는 수를 알고 싶다.

start = 1
end = k

res = 0

while start <= end:
    mid = (start + end) // 2

    temp = sum(min(mid//i, n) for i in range(1, n+1))
    if temp >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1


print(res)