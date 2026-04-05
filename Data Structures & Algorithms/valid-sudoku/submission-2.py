class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sqr = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                if board[i][j] in sqr[i//3][j//3]:
                    return False
                sqr[i//3][j//3].add(board[i][j])
        return True
