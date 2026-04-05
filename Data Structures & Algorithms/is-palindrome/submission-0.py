class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_s = ''.join([c.lower() for c in s if c.isalnum()])
        l, r = 0, len(sorted_s)-1
        while l < r:
            if sorted_s[l] != sorted_s[r]:
                return False
            l += 1
            r -= 1
        return True