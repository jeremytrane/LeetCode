class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_mul = []
        post_mul = []
        N = len(nums)

        total = 1
        for i in range(N):
            total *= nums[i]
            pre_mul.append(total)

        total = 1
        for i in range(N-1, -1, -1):
            total *= nums[i]
            post_mul.append(total)
        post_mul.reverse()

        res = []
        for i in range(N):
            if i < 1:
                res.append(1*post_mul[i+1])
            elif i >= 1 and i <= N-2:
                res.append(pre_mul[i-1]*post_mul[i+1])
            else:
                res.append(pre_mul[i-1]*1)
        return res