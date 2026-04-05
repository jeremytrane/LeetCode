class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        def countPalindroms(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return 

        for i in range(n):
            countPalindroms(i, i)
        for i in range(n-1):
            countPalindroms(i, i+1)
        return count