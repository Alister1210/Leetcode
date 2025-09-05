# 36 Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
class Solution(object):
    def isValidSudoku(self, board):
        n=9
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                print(val)
                if val == '.':
                    continue
                if val in row[i] or val in col[j] or val in box[i//3,j//3]:
                    return False
                row[i].add(val)
                col[j].add(val)
                box[i//3,j//3].add(val)
        return True
        