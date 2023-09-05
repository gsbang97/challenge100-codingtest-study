import sys

N = int(sys.stdin.readline())
p_list = sorted(map(int, sys.stdin.readline().split()))
tot_time = 0
accumulate_time = 0

for p in p_list:
    accumulate_time += p
    tot_time += accumulate_time

#print(p_list)
print(tot_time)
