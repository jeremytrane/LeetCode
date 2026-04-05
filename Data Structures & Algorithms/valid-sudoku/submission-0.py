class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_len = len(board[0])
        col_len = len(board)

        rows = [set() for _ in range(row_len)]
        cols = [set() for _ in range(col_len)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(row_len):
            for j in range(col_len):

                if board[i][j] == ".":
                    continue
                    
                else:

                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])

                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])

                    if board[i][j] in squares[i//3][j//3]:
                        return False
                    squares[i//3][j//3].add(board[i][j])

        return True