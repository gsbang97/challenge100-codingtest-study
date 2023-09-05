import sys

N = int(sys.stdin.readline())
n_list = []

for _ in range(N):
    cur_num = int(sys.stdin.readline())
    n_list.append(cur_num)

n_list.sort()

for i in n_list:
    print(i)