class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited = set()
            visited.add((r,c))
            length = 0

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return length

                    for dr, dc in directions:
                        if (min(r + dr, c + dc) < 0 or
                            r + dr == ROWS or c + dc == COLS or
                            (r + dr, c + dc) in visited or grid[r + dr][c + dc] == -1):
                            continue
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

                length += 1
            return 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c)
