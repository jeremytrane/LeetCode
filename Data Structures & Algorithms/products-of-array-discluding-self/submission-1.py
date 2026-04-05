class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preMul = []
        postMul = []
        N = len(nums)

        total = 1
        for i in range(N):
            total *= nums[i]
            preMul.append(total)

        total = 1
        for i in range(N-1, -1, -1):
            total *= nums[i]
            postMul.append(total)
        postMul.reverse()

        res = []
        for i in range(N):
            if i == 0:
                res.append(postMul[i+1])
            elif i < N-1:
                res.append(preMul[i-1] * postMul[i+1])
            elif i == N-1:
                res.append(preMul[i-1])
        return res