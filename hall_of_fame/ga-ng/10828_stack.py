import sys

input = sys.stdin.readline

n = int(input())

stack = []

command = [input().rstrip() for _ in range(n)]
# print(command)

for i in command:
    if i == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif i == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif i == "size":
        print(len(stack))
    elif i == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(i[5:])