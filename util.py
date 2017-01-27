from setup import *

def display(sudoku):
    """
    Display the sudoku as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1 + max(len(sudoku[s]) for s in BOXES)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in ROWS:
        print(''.join(sudoku[r + c].center(width) + ('|' if c in '36' else '')
                      for c in COLS))
        if r in 'CF': print(line)
    print

def parse_sudoku_string(sudoku_string):
    """
    Convert the string representation into a dict of {box: string} with '123456789' for empties.
    Input: The sudoku in string form.
    Output: The sudoku in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    keys = ( convert_position(pos) for pos in range(len(sudoku_string) ))
    return { k: v if v is not '.' else COLS for k, v in zip(keys, sudoku_string) }

def convert_position(pos):
    return(ROWS[pos // len(ROWS)] + COLS[pos % len(COLS)])

if __name__ == '__main__':
    grid = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
    display(parse_sudoku_string(grid))
    print(parse_sudoku_string(grid))
