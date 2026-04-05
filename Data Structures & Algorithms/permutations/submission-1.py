class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            if i >= len(nums):
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(i, path)
                path.pop()

        backtrack(0, [])
        return res