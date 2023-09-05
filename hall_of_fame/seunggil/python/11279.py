import heapq
import sys

n = int(sys.stdin.readline().rstrip())

maxQueue = []
for _ in range(n):
    query = int(sys.stdin.readline().rstrip())
    if query > 0:
        heapq.heappush(maxQueue,-query)
    elif maxQueue:
        print(-heapq.heappop(maxQueue))
    else:
        print(0)