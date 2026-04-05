class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            length = 1

            if num - 1 in num_set:
                continue
            
            while num + 1 in num_set:
                num += 1
                length += 1
            max_length = max(max_length, length)

        return max_length