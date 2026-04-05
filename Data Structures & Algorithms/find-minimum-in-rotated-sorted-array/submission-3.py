class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        if nums[l] < nums[r] or len(nums)<2:
            return nums[l]

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[l]:
                l = m
            else:
                r = m
            
        return nums[l+1]