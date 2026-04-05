class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ''
        for word in strs:
            encode_string += f'#{len(word)}#{word}'
        return encode_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                j = i + 1
                # Find the next '#' which separates the length from the word
                while s[j] != '#':
                    j += 1
                length = int(s[i + 1:j])
                word = s[j + 1: j + 1 + length]
                res.append(word)
                i = j + 1 + length
            else:
                i += 1
        return res