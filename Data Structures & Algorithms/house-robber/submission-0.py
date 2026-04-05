class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        one, two = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            one, two = two, max(two, one + nums[i])
        return max(one, two)
