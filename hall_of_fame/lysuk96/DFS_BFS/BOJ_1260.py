#DFS와 BFS
from collections import deque, defaultdict
import sys

N, M, start = map(int, input().split())
edge = defaultdict(list)
for _ in range(M):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for value in edge.values():
    value.sort()

d_check = []
def dfs(x):
    if x in d_check:
        return
    print(x, end=' ')
    d_check.append(x)
    for i in edge[x]:
        dfs(i)

b_check =[start]
queue = deque([start])
def bfs():
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in edge[v]:
            if i not in b_check:
                queue.append(i)
                b_check.append(i)

dfs(start)
print()
bfs()
