import sys

N = int(sys.stdin.readline())
lope_list = [int(sys.stdin.readline()) for _ in range(N)]
lope_list.sort()
max_mass = 0
for cnt, lope in enumerate(lope_list):
    cur_mass = lope * (N-cnt)

    if cur_mass > max_mass:
        max_mass = cur_mass

print(max_mass)
    