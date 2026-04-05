class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        start = 0
        length = 0
        maxLength = 0

        for end in range(len(s)):
            charMap[s[end]] += 1
            length += 1
            while (end - start - max(charMap.values())) >= k:
                charMap[s[start]] -= 1
                length -= 1
                start += 1
            maxLength = max(maxLength, length)
        return maxLength
