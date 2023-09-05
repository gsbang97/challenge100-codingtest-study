# https://www.acmicpc.net/problem/1744
from collections import deque
N = int(input())

num = [int(input()) for _ in range(N)]
q = deque(sorted(num))
answer =0
while q:
    if q[0]<=0:
        tmp = q.popleft()
        answer += tmp*q.popleft() if q and q[0] <= 0 else tmp
    elif q[0] == 1:
        answer+=q.popleft()
    else:
        tmp = q.pop()
        answer += tmp*q.pop() if q else tmp
print(answer)
    
        

