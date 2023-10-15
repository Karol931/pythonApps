import numpy as np
import random

def create():
    sudoku = np.zeros((9,9),dtype=int)
    randomize_sudoku(sudoku)
    remove_cells(sudoku)
    return sudoku

def randomize_sudoku(sudoku):
    if not check_empty(sudoku):
        return True

    row, col = check_empty(sudoku)

    number_list = random.sample(range(10), 10)
    print(sudoku)
    for number in number_list:
        if is_valid(sudoku, row, col, number):
            sudoku[row][col] = number
            print(sudoku)
            if randomize_sudoku(sudoku):
                return True

            sudoku[row][col] = 0

    return False


def remove_cells(sudoku, num_to_remove = 45):
    removed_cells = set()
    
    while len(removed_cells) < num_to_remove:
        row = random.randint(0,8)
        col = random.randint(0,8)

        if (row, col) not in removed_cells:
            sudoku[row][col] = 0
            removed_cells.add((row,col))

    return sudoku

def solver(sudoku):
    if not check_empty(sudoku):
        return True

    row, col = check_empty(sudoku)

    for number in range(1,10):
        if is_valid(sudoku, row, col, number):
            sudoku[row][col] = number

            if solver(sudoku):
                return True

            sudoku[row][col] = 0

    return False

def check_empty(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col

    return None


def is_valid(sudoku, row, col, number):
    #Check rows
    if number in sudoku[row]:
        return False

    #Check columns
    if number in [sudoku[r][col] for r in range(9)]:
        return False

    #Check boxes
    start_row = row - row % 3
    start_col = col - col % 3
    if number in [
        sudoku[r][c]
        for r in range(start_row, start_row + 3)
        for c in range(start_col, start_col + 3)
    ]:
        return False

    return True
