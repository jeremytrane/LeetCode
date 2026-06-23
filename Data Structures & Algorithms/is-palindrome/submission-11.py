class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        sanitizeString = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(sanitizeString)-1
        while l < r:
            if sanitizeString[l] != sanitizeString[r]:
                return False
            l += 1
            r -= 1
        return True