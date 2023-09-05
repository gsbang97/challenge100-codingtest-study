import sys

class Solution:
    def expand(self, right, s):
        while self >= 0 and right < len(s) and s[self] == s[right]:
            self -= 1
            right += 1

        return s[self + 1:right]

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        ans = ''
        for i in range(len(s)):
            ans = max(ans, Solution.expand(i, i+1, s), Solution.expand(i, i+2, s), key = len)        

        return ans
        
sol = Solution()
print(sol.longestPalindrome(s = "cbbd"))