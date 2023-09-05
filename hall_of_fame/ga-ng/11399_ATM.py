n = int(input())

time_list = sorted(map(int, input().split()))
time = 0
sum = 0
for i in time_list:
    sum += i
    time += sum

print(time)