import sys

max_range_n = 123456
plist = [True for _ in range(2*max_range_n + 1)]
plist[1] = False

for cur_num in range(2, max_range_n+1) :
        if plist[cur_num] == True:
            for mul_num in range(2, 2*max_range_n+1) :
                if cur_num * mul_num > 2*max_range_n :
                    break
                plist[cur_num * mul_num] = False


N = int(sys.stdin.readline())

while True:    
        prime_cnt = sum(1 for i in range(N+1, 2*N + 1) if plist[i] == True)
        print(prime_cnt)

        N = int(sys.stdin.readline())

        if N == 0 :
            break