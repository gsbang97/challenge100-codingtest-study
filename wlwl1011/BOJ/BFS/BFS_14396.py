import sys, io, os, atexit
input = lambda : sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda : os.write(1,stdout.getvalue()))
from collections import deque
s, t = map(int, input().split())



if s==t:
    print(0)
else:
    queue = deque()
    visited = set()
    queue.append((s,''))
    flag = True
    while queue:
        x, cnt = queue.popleft()
        #print(x,cnt)
        if x == t:
            flag = False
            print(cnt)
            break
        if x * x <= t and x * x not in visited:
            visited.add(x*x)
            queue.append((x*x, f'{cnt}*'))
        if x + x <= t and x + x not in visited:
            visited.add(x+x)
            queue.append((x+x, f'{cnt}+'))
        if x - x not in visited:
            visited.add(x-x)
            queue.append((x-x, f'{cnt}-'))
        if x != 0 and x // x not in visited:
            visited.add(x//x)
            queue.append((x//x, f'{cnt}/'))
    if flag:
        print(-1)


