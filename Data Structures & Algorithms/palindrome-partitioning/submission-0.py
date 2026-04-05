class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isValidPalindrome(path) -> bool:
            l, r = 0, len(path) - 1
            while l < r:
                if path[l] != path[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i, path):
            if i >= len(s):
                res.append(path.copy())
                return

            if i >= len(s):
                return

            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if isValidPalindrome(sub):
                    path.append(sub)
                    backtrack(j + 1, path)
                    path.pop()

        backtrack(0, [])
        return res