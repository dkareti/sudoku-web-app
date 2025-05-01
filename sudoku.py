#Generate the helper functions to be used by the flask app


import random
import copy

# checks for valid placement of a number at the specified row
# and column of the grid
def is_valid(grid, row: int, col: int, num: int) -> bool:
    #   #   #   #   #   #   #   #   #   #
    # check the row and column to make sure 
    # the rules of sudoku are followed
    #   #   #   #   #   #   #   #   #   #   
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    #   #   #   #   #   #   #   #   #   #   
    # check the 3x3 sub-grid
    # the following line finds the top-left corner of the 3x3
    #   subgrid
    #
    # For Example,
    # If row = 5, col = 7, then:
	#   •	row // 3 = 1, so start_row = 3 * 1 = 3
	#   •	col // 3 = 2, so start_col = 3 * 2 = 6
    #
    #   #   #   #   #   #   #   #   #   # 
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col+3):
            if grid[i][j] == num:
                return False
    return True

