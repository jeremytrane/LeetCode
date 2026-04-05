class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {} 
        for i, num in enumerate(nums):
            diff = target - num
            if diff in myHash:
                return [myHash[diff], i]
            myHash[num] = i
        return [-1, -1]