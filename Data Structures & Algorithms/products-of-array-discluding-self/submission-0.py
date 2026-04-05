class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_mul = []
        post_mul = []
        total = 1

        #pre mul
        for num in nums:
            total *= num
            pre_mul.append(total)
        
        #post mul
        total = 1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            post_mul.append(total)
        post_mul.reverse()
        # post_mul = sorted(post_mul, reverse=True)

        res = []
        for i in range(len(nums)):
            if i < 1 :
                res_append = 1*post_mul[i+1]
            elif i >= 1 and i < len(nums)-1:
                res_append = pre_mul[i-1]*post_mul[i+1]
            else:
                res_append = pre_mul[i-1]*1
            res.append(res_append)
        return res

