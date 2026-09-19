class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = j =0
        word_len = 0
        while i < len(s):
            if s[i] == "#":
                word_len = int(s[j:i])
                decoded_string.append(s[i+1:i+1+word_len])
                i += word_len + 1
                j = i
            i += 1
        return decoded_string