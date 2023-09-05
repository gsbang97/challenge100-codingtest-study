import sys
import heapq

N = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(N)]
card.sort()

pq = list(card)
sum = 0
cmp_cnt = 0
while len(pq) > 1:
    sum = heapq.heappop(pq) + heapq.heappop(pq)
    cmp_cnt += sum
    pq.append(sum)

print(cmp_cnt)
