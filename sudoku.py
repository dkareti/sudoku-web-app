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

def solve_grid(grid):
    #implement recursion
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_grid(grid):
                            #   #   #   #   #   #   
                            # check to see if the entire 
                            #  puzzle can be solved by adding
                            #  this value.
                            #   #   #   #   #   #   
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_full_grid():
    #   #   #   #   #   #   
    # Generates a valid 9x9 sudoku board, completely filled
    #   #   #   #   #   #   
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_grid(grid)
    return grid

###################################
# With a complete 9x9 sudoku board
#  we need to remove numbers based
#  on the user's specified difficulty 
#  level
###################################

def remove_numbers(grid, difficulty):
    holes_by_lvl = {
        'Easy': 30,
        'Medium': 40,
        'Hard': 50
    }

    #the default difficulty is Easy
    holes = holes_by_lvl.get(difficulty, 30)
    puzzle = copy.deepcopy(grid)

    removed = 0
    while removed < holes:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1
    
    return puzzle

