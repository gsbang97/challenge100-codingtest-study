N = int(input())
times = sorted(map(int, input().split(" ")))
answer = sum((N-i)*time for i, time in enumerate(times))
print(answer)