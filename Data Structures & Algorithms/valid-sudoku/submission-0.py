class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = set()
        y = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(9):
            x = set()
            for j in range(9):
                box = (i // 3) * 3 + (j // 3)
                if board[i][j].isdigit():
                    if board[i][j] in x or board[i][j] in y[j] or board[i][j] in squares[box]:
                        return False        
                    x.add(board[i][j])
                    y[j].add(board[i][j])
                    squares[box].add(board[i][j])
        return True


