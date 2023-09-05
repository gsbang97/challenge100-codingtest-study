import sys

N = int(sys.stdin.readline())
cnt = 0
cur_num = 666

while cnt < N-1:
    cur_num += 1

    if "666" in str(cur_num):
        cnt += 1

print(cur_num)
    