class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_defaultdict = defaultdict(int)
        t_defaultdict = defaultdict(int)
        
        for i in range(len(s)):
            s_defaultdict[s[i]] += 1
            t_defaultdict[t[i]] += 1

        return s_defaultdict == t_defaultdict