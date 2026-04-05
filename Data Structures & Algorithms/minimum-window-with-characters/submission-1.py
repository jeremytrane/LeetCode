class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        sCount = defaultdict(int)
        tCount = Counter(t)

        have, need = 0, len(tCount)
        res = ""
        resLen = float("inf")
        start = 0
        for end in range(len(s)):
            sCount[s[end]] += 1
            if s[end] in tCount and sCount[s[end]] == tCount[s[end]]:
                have += 1

            while have == need:
                if (end-start+1) < resLen:
                    res = s[start:end+1]
                    resLen = (end-start+1)
                sCount[s[start]] -= 1

                if s[start] in tCount and sCount[s[start]] < tCount[s[start]]:
                    have -= 1
                start += 1
        return res
