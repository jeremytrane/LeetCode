class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l <= r:
            m = (l+r)//2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/m)
            if time > h:
                l = m + 1
            else:
                r = m - 1
        return l