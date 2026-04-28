class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countNums = Counter(nums)

        return sorted(countNums.keys(), reverse=True, key=lambda x:countNums[x])[:k]