class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = 0
        res = []
        for i in range(n+1):
            while i > 0:
                if i & 1 == 1:
                    counter += 1
                i = i >> 1
            res.append(counter)
            counter = 0
        return res
