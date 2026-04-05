class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(sNew)-1

        while l < r:
            if sNew[l] != sNew[r]:
                return False
            l += 1
            r -= 1
        return True