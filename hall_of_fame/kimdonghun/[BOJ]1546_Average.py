import sys

N = int(input())
myList = list(map(int, sys.stdin.readline().split(' ')))

#print(myList)

sum = 0
avg = 0
myMax = max(myList)

for item in myList:
    sum += item / myMax * 100
    #print(sum)

avg = sum / N
print(avg)
