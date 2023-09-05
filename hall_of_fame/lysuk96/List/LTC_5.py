class Solution:
    def longestPalindrome(self, s: str) -> str:
        
    def expand(self, right:int) -> str:
        while self >= 0 and right < len(s) and s[self] == s[right]:
            self -= 1
            right += 1
        return s[self + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i,i+1),expand(i,i+2), key=len)

    return result