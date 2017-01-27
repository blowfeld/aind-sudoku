updates = None

def update(sudoku):
    if updates is not None and sudoku:
        updates.append(sudoku.copy())
