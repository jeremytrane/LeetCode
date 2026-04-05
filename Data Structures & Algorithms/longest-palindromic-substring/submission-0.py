class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        def palindromeLength(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(res) < r - l + 1:
                    res = s[l:r+1]
                l -= 1
                r += 1
            return 

        for i in range(n):
            palindromeLength(i, i)
        for i in range(n-1):
            palindromeLength(i, i+1)
            
        return res