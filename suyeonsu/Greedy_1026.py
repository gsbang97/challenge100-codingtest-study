n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()
answer = sum(a*b for a, b in zip(A, B))
print(answer)
