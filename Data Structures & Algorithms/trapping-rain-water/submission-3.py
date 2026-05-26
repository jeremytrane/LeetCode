class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        Lmax, Rmax = height[l], height[r]
        res = 0

        while l < r:
            if Lmax < Rmax:
                if height[l+1] > Lmax:
                    Lmax = height[l+1]
                else:
                    res += (Lmax-height[l+1])
                l += 1
            else:
                if height[r-1] > Rmax:
                    Rmax = height[r-1]
                else:
                    res += (Rmax-height[r-1])
                r -= 1
        return res

