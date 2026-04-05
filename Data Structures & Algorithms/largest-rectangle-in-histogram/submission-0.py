class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        stack = [] # (index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                lastIndex, lastHeight = stack.pop()
                max_area = max(max_area,lastHeight*(i-lastIndex))
                start = lastIndex
            stack.append((start, height))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area