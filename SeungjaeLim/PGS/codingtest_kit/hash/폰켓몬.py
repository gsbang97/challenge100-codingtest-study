def solution(nums):
    answer = 0
    target = len(nums) // 2

    dex = set(nums)

    return min(len(dex), target)
