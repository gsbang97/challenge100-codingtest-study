from collections import defaultdict, deque
N = int(input())
M = int(input())
coms = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split(" "))
    coms[x].append(y)
    coms[y].append(x)
# print(coms)

q = deque([1])
visit = [False]*(N+1)
while q:
    tmp = q.popleft()
    for com in coms[tmp]:
        if not visit[com]:
            visit[com] = True
            q.append(com)

answer = sum(1 for flag in visit if flag)
print(answer-1)
