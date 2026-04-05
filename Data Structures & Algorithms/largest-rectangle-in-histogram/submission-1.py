class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [height, index]  
        maxArea = 0

        for i, height in enumerate(heights):
            area = 0
            start = i
            while stack and height < stack[-1][0]:
                h, idx = stack.pop()
                area = h*(i-idx)
                maxArea = max(maxArea, area)
                start = idx
            stack.append([height, start])

        N = len(heights)
        for i in range(len(stack)):
            h, idx = stack.pop()
            area = h*(N-idx)
            maxArea = max(maxArea, area)
        return maxArea