class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chat_count = defaultdict(int)
        max_length = 0
        length = 0
        start = 0

        for i, letter in enumerate(s):
            chat_count[letter] += 1
            length += 1
            while chat_count[letter] > 1:
                chat_count[s[start]] -= 1
                start += 1
                length -= 1
            max_length = max(max_length, length)
        return max_length