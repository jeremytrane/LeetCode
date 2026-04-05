class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # Stores (r, c)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            return 1 + sum(dfs(r + dr, c + dc) for dr, dc in directions)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))

        return area