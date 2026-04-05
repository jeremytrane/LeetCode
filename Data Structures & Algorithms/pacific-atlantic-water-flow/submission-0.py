class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(source):
            visited = set(source)
            q = deque(source)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return visited

        for r in range(ROWS):
                pac.add((r, 0))
                atl.add((r, COLS-1))

        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS-1, c))

        pac = bfs(pac)
        atl = bfs(atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])
        return res