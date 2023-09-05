import sys

def factorial(a):
    return 1 if (a == 0) else a * factorial(a-1)

N = int(sys.stdin.readline())

print(factorial(N))

    