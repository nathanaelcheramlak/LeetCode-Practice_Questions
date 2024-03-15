# Problem 36 - Valid Sudoku

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

def validSoduku(board):
    # Checks the row.
    for i in board:
        seen = set()
        for j in i:
            if j in seen:
                return False
            if j != '.':
                seen.add(j)
            
    # Checks Columns.
    for i in range(9):
        seen = set()
        for j in range(9):
            if board[j][i] in seen:
                return False
            if board[j][i] != '.':
                seen.add(board[j][i])
    
    # Checks Boxes.
    coordinates = [(0,0), (3,0), (6,0),
                   (0,3), (3,3), (6,3),
                   (0,6), (3,6), (6,6)]
    for i, j in coordinates:
        seen = set()
        for col in range(i, i+3):
            for row in range(j, j+3):
                item = board[col][row]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
    return True
            
# Test Case

# board = [[".",".","4",".",".",".","6","3","."],
#          [".",".",".",".",".",".",".",".","."],
#          ["5",".",".",".",".",".",".","9","."],
#          [".",".",".","5","6",".",".",".","."],
#          ["4",".","3",".",".",".",".",".","1"],
#          [".",".",".","7",".",".",".",".","."],
#          [".",".",".","5",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."]]
# print(validSoduku(board))

# Time Complexity: O(1) - given that it is a 3X3 grid
# Space Complexity: O(1)
