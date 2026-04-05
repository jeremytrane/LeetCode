class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k < 1 or not nums:
            return []

        res = []
        q = deque()
        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
            
        return res