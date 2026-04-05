class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = 0
        def cyclicalNumber(n):
            total = 0
            digits = [int(digit) for digit in str(n)]
            for digit in digits:
                total += digit*digit
            return total
        while n != 1:
            n = cyclicalNumber(n)
            if n in seen:
                return False
            seen.add(n)
        return True