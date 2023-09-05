def solution(arr):
    ans = []
    top = -1
    for i in arr:
        if top == -1 or ans[top] != i:
            ans.append(i)
            top += 1
    return ans
