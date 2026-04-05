class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # Stores (r, c)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = area = 0

        def dfs(r, c):
            nonlocal area
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                visited.add((r, c))
                area += 1
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea