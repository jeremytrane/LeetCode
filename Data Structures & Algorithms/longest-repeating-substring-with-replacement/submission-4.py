class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCount = defaultdict(int)
        length = maxLength = 0
        start = 0

        for c in s:
            length += 1
            charCount[c] += 1

            while length - max(charCount.values()) > k:
                charCount[s[start]] -= 1
                start += 1
                length -= 1
            maxLength = max(maxLength, length)
        return maxLength