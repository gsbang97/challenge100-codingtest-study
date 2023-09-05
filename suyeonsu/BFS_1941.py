from collections import deque
from itertools import combinations

board = [list(input()) for _ in range(5)]
answer = 0


def checkCount(comb):
    cnt = sum(1 for x, y in comb if board[x][y] == 'S')
    return cnt >= 4


def checkAdj(comb):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [0] * 7

    dq = deque([comb[0]])
    visited[0] = 1
    while dq:
        x, y = dq.popleft()
        for d in zip(dx, dy):
            nx, ny = x+d[0], y+d[1]
            if (nx, ny) in comb and not visited[comb.index((nx, ny))]:
                dq.append((nx, ny))
                visited[comb.index((nx, ny))] = 1
    return sum(visited) == 7


for comb in list(combinations([(i, j) for i in range(5) for j in range(5)], 7)):
    if checkCount(comb) and checkAdj(comb):
        answer += 1
print(answer)
