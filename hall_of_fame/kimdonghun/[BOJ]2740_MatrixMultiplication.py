import sys

N, M = map(int, sys.stdin.readline().split())
N_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#print(N_matrix)

M, K = map(int, sys.stdin.readline().split())
M_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
#print(M_matrix)

R_matrix = []

for i in range(N):
    tmp_l = []

    for k in range(K):
        
        res = sum(N_matrix[i][j] * M_matrix[j][k] for j in range(M))
        tmp_l.append(res)

    R_matrix.append(tmp_l)

for l in R_matrix:
    print(*l)
