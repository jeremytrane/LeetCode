class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        numSet = set(nums)
        maxCount = 0 
        for num in numSet:
            count = 1
            if num - 1 in numSet:
                continue
            while num + 1 in numSet:
                num += 1
                count += 1
            maxCount = max(maxCount, count)
        return maxCount