import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque(list(range(1, N+1)))
#print(q)

cnt = 0
while (len(q) >= 2):
    if cnt % 2 != 0:
        q.append(q[0])
    q.popleft()
    cnt += 1

print(q[0])
