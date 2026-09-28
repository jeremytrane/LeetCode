class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_mul = []
        post_mul = []
        res = []

        total = 1
        for num in nums:
            total *= num
            pre_mul.append(total)

        
        total = 1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            post_mul.append(total)
        post_mul.reverse()

        # [1, 2, 8, 24]
        # [48, 48, 24, 6]
        for i in range(len(nums)):
                res.append(post_mul[i+1]) if i == 0 else (
                res.append(pre_mul[i-1]) if i == len(nums)-1 else
                res.append(pre_mul[i-1] * post_mul[i+1])
            )

        return res