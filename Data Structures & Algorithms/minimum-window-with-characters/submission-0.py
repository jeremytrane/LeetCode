class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        if not s or not t:
            return "" 

        count_t = defaultdict(int)
        for letter in t:
            count_t[letter] += 1

        count_s = defaultdict(int)
        have = 0
        need = len(count_t)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r, letter in enumerate(s):
            count_s[letter] += 1

            if letter in count_t and count_t[letter] == count_s[letter]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
                