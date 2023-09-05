import sys
import sys

n = int(sys.stdin.readline().rstrip())

count = {}
maxCount = 0
sum = 0
data = []

for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    if m in count:
        count[m] += 1
    else :
        count[m] = 1
    maxCount = max(maxCount, count[m])
    sum += m
    data.append(m)

data.sort()
print(round(sum/n))
print(data[n//2])

mostShow = [i for i, count in count.items() if count == maxCount]
mostShow.sort()
if len(mostShow) == 1:
    print(mostShow[0])
else:
    print(mostShow[1])

print(data[-1] - data[0])