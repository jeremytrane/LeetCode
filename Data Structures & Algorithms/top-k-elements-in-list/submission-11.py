class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        return sorted(count.keys(), reverse=True, key=lambda x:count[x])[:k]