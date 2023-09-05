
def fib(n):
    global cnt2

    if n in [1, 2]:
        return 1
    cnt2 += 1
    return fib(n-1) + fib(n-2)
    
def fibonacci(n):
    return len(range(3,n+1))


n = int(input())
cnt2 = 1


fib(n)
print(cnt2, fibonacci(n))