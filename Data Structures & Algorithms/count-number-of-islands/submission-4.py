class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or c == COLS or r == ROWS or (r, c) in visited or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                visited.add((r, c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands