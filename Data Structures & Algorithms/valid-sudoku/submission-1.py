class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filtered = [val for val in row if val != "."]
            if len(filtered) != len(set(filtered)): return False
        for col in zip(*board):
            col = list(col)
            fil_col = [val for val in col if val != "."]
            if len(fil_col) != len(set(fil_col)): return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                sub_box = [board[i][j] for i in range(row, row+3) for j in range(col, col+3)]
                fil_sub_box = [val for val in sub_box if val != "."]
                if len(fil_sub_box) != len(set(fil_sub_box)): return False
        return True    
            
        