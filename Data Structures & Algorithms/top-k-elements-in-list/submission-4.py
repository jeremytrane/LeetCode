class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # digit, frequency
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        return list(sorted(count.keys(), key=lambda x: count[x], reverse=True))[:k]
        