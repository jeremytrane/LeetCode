class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index, height
        maxArea = 0
        area = 0
        for i, height in enumerate(heights):
            
            start = i 

            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                area = (i-idx)*h
                maxArea = max(maxArea, area)
                start = idx
            stack.append([start, height])

        while stack:
            idx, h = stack.pop()
            area = (len(heights)-idx)*h
            maxArea = max(maxArea, area)
        return maxArea