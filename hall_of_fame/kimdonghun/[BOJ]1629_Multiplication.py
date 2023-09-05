import sys

A,B,C = map(int, sys.stdin.readline().split())

def solution(a, b, c):
    if b == 1:
        return a % c

    tmp_res = solution(a, b // 2, c)

    return tmp_res * tmp_res % c if b % 2 == 0 else tmp_res * tmp_res * a % c

print(solution(A,B,C))
