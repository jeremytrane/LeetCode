class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        def helper(start, end):
            if start == end:
                return nums[start]
            one, two = nums[start], max(nums[start], nums[start+1])
            for i in range(start+2, end + 1):
                one, two = two, max(two, one + nums[i])
            return two

        return max(helper(0, n-2), helper(1, n-1))