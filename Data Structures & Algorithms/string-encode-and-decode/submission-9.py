class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string  = ''
        for word in strs:
            encoded_string += f'{len(word)}#{word}'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        word_len = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            decoded_string.append(s[j+1:j+1+word_len])
            i = j+1+word_len
        return decoded_string
