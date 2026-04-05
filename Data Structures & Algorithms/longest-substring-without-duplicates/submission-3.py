class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chat_hash = defaultdict(int)
        max_length = 0
        length = 0
        start = 0

        for i, letter in enumerate(s):
            chat_hash[letter] += 1
            if chat_hash[letter] < 2:
                length += 1
                max_length = max(max_length, length)
            else:
                while s[start] != letter:
                    chat_hash[s[start]] -= 1
                    start += 1
                    length -= 1
                chat_hash[s[start]] -= 1
                start += 1
                max_length = max(max_length, length)

        return max_length