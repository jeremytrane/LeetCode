class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = {} # num, index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_set:
                return [my_set[diff], i]
            my_set[num] = i