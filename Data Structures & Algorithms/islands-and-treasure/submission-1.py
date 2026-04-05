from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        INF = 2147483647
        q = deque()

        # Step 1: Enqueue all treasure cells (0s)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: BFS from all treasures simultaneously
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip out-of-bounds, walls, or already visited cells
                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    grid[nr][nc] != INF):
                    continue

                # Update distance and add to queue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))