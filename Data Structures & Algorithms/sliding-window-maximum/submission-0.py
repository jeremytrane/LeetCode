class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        window = deque()
        res = []

        for i in range(k):
            window.append(nums[i])
        res.append(max(window))

        for i in range(k-1, len(nums)-1):
            window.popleft()
            window.append(nums[i+1])
            res.append(max(window))

        return res