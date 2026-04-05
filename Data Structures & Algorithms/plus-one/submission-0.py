class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = ""
        for digit in digits:
            total += str(digit)
        total = int(total) + 1
        total = str(total)
        res = []
        for i in range(len(total)):
            res.append(int(total[i]))
        return res
        