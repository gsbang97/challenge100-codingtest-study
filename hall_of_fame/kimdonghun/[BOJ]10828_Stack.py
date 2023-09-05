import sys

class stack:
    s = []

    def push(self, X):
        self.s.append(X)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            print(self.s.pop())

    def size(self):
        return len(self.s) 

    def empty(self):
        return 1 if (self.size() == 0) else 0

    def top(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.s[-1])

N = int(sys.stdin.readline())
s = stack()

for _ in range(N):
    cmd_list = list(sys.stdin.readline().split())

    if cmd_list[0] == "push":
        num = int(cmd_list[1])
        #print(num)
        s.push(num)
    elif cmd_list[0] == "pop":
        s.pop()
    elif cmd_list[0] == "size":
        print(s.size())
    elif cmd_list[0] == "empty":
        print(s.empty())
    elif cmd_list[0] == "top":
        s.top()

    #print(cmd_list)
