# https://inha.codetree.ai/missions/2/problems/max-area-of-positive-rectangle?&utm_source=clipboard&utm_medium=text
# n 입력받기
n = int(input())
result = 0
# n x n 행렬 입력받기
mat = [list(map(int, input().split())) for _ in range(n)]
# 3 x 3 행렬의 좌측 상단 좌표를 (i, j)라고 하면, i, j는 각각 0부터 n-3까지의 값을 가질 수 있다.
# (i, j)가 (0, 0)일 때, 3 x 3 행렬의 원소들의 합을 coin이라고 할 때, coin의 최대값을 구하면 된다.
# (i, j)가 (1, 0)일 때, 3 x 3 행렬의 원소들의 합을 coin이라고 할 때, coin의 최대값을 구하면 된다.
# ...
# (i, j)가 (n-3, n-3)일 때, 3 x 3 행렬의 원소들의 합을 coin이라고 할 때, coin의 최대값을 구하면 된다.
# (i, j)가 (n-2, n-2)일 때, 3 x 3 행렬의 원소들의 합을 coin이라고 할 때, coin의 최대값을 구하면 된다.
# 따라서 i, j는 각각 0부터 n-3까지의 값을 가질 수 있다.
for i in range(n-2):
    for j in range(n-2):
        coin = 0
        # (i, j)를 좌측 상단 좌표로 하는 3 x 3 행렬의 원소들의 합을 구한다.
        for k in mat[i:i+3]:
            coin += sum(k[j:j+3])
        # coin의 최대값을 구한다.
        if result < coin:
            result = coin
# coin의 최대값을 출력한다.
print(result)