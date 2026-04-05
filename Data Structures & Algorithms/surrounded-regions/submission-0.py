class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1 ,0] ,[-1 ,0], [0, 1], [0, -1]]
        q = deque()

        for r in range(ROWS):
            if board[r][0] == "O" and (r, 0) not in q:
                board[r][0] = "T"
                q.append((r, 0))
            if board[r][COLS-1] == "O" and (r, COLS-1) not in q:
                board[r][COLS-1] = "T"
                q.append((r, COLS-1))

        for c in range(COLS):
            if board[0][c] == "O" and (0, c) not in q:
                board[0][c] = "T"
                q.append((0, c))
            if board[ROWS-1][c] == "O" and (ROWS-1, c) not in q:
                board[ROWS-1][c] = "T"
                q.append((ROWS-1, c))
        print(q)

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or board[nr][nc] == "X":
                    continue
                if board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

