import sys

A,B,C = map(int, sys.stdin.readline().split())
#print(A,B,C)

same_num = 0
if A in [B, C]:
    same_num = A

    print(1000 + same_num * 100)
elif B == C:
    same_num = B

    print(1000 + same_num * 100)
else:
    print(max(A,B,C) * 100)
