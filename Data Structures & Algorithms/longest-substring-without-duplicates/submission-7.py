class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = defaultdict(int)
        maxLength = 0
        length = 0
        start = 0
        for c in s:
            charMap[c] += 1
            length += 1
            while charMap[c] > 1:
                charMap[s[start]] -= 1
                length -= 1
                if charMap[s[start]] == 0:
                    del charMap[s[start]]
                start += 1
            maxLength = max(maxLength, length)
        return maxLength