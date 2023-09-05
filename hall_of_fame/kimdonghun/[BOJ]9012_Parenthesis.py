import sys

T = int(sys.stdin.readline())

for _ in range(T):
    p_list = list(sys.stdin.readline()[:-1])
    #print(p_list)

    s = []
    isVPS = True
    for p in p_list:
        if p == '(':
            s.append('(')
        elif s:
            s.pop()
        else:
            isVPS = False

    #print(s)
    #print(isVPS)

    if s or isVPS == False:
        print("NO")
    else:
        print("YES")
