class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        max_length = 0
        length = 0
        start = 0

        for i, letter in enumerate(s):
            char_count[letter] += 1
            while (i - start + 1) - max(char_count.values()) > k:
                char_count[s[start]] -= 1
                start += 1
                length -= 1
            length += 1
            max_length = max(max_length, length)
        return max_length