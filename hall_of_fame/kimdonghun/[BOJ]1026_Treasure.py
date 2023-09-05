import sys

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

A_list.sort()
B_max_list = sorted(B_list, reverse=True)

ans = sum(A * B_max_list[i] for i, A in enumerate(A_list))
#print(A_list)
#print(B_max_list)

print(ans)