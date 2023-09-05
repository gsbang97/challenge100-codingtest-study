
equation = input().split('-')

num = []

for i in equation:
    s = i.split('+')
    temp = sum(int(j) for j in s)
    num.append(temp)

ans = num[0]*2

for i in num:
    ans -= i

print(ans)