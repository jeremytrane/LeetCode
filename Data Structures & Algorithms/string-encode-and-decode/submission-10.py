class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += f'{word}###!'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        splitS = s.split('###!')
        for word in splitS:
            res.append(word)
        res.pop()
        return res

