class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCount = defaultdict(int)
        maxLength = length = 0
        start = 0
        for i, char in enumerate(s):
            length += 1
            charCount[char] += 1
            while charCount[char] > 1:
                charCount[s[start]] -= 1
                length -= 1
                start += 1
                if charCount[s[start]] == 0:
                    del charCount[s[start]]
            maxLength = max(maxLength, length)
        return maxLength