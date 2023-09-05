for _ in range(int(input())):
    answer = sum(len(o)*(len(o)+1)//2 for o in list(input().split('X')))
    print(answer)
