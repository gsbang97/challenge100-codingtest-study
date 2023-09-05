import sys

def draw_star(n, l):
    if n == 3:
        return l
    ans = [i * 3 for i in l]
    ans.extend(i + ' ' * len(l) + i for i in l)
    ans.extend(i * 3 for i in l)
    #print(ans)

    return draw_star(n//3, ans)
    

N = int(sys.stdin.readline())
base = ['***', '* *', '***']
res = draw_star(N, base)

for i in res:
    print(i)