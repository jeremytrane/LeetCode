class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        area = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                if height[l] > lMax:
                    lMax = height[l]
                else:
                    area += lMax - height[l]
            else:
                r -= 1
                if height[r] > rMax:
                    rMax = height[r]
                else:
                    area += rMax - height[r]
        return area