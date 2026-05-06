class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])

                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if board[r][c] in squares[r//3][c//3]:
                    return False
                squares[r//3][c//3].add(board[r][c])
        return True