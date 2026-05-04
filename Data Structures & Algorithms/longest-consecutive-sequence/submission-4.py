class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        my_set = set(nums)
        maxLength = 0
        for num in my_set:
            length = 1
            if num - 1 in my_set:
                continue
            else:
                while num + 1 in my_set:
                    length += 1
                    num += 1
            maxLength = max(maxLength, length)
        return maxLength