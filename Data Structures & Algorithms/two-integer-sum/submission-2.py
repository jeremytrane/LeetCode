class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_set = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_set:
                return [my_set[diff], i]
            my_set[n] = i

        return [-1, -1]
