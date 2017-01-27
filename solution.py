"""
This module solely provides a wrapper to make the code in the imported modules
compliant with the expected solution format. For implementations and method
documentation please refer to the imported modules.

This choice was made to make the code more structured and avoid the naming
inconsistencies in this module.
"""

import setup
import strategy
import ui
import util

assignments = []
ui.updates = assignments

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    return strategy.naked_twins(values)

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [ s + t for s in A for t in B ]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return util.parse_sudoku_string(grid)

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    util.display(values)

def eliminate(values):
    return strategy.eliminate(values)

def only_choice(values):
    return strategy.only_choice(values)

def reduce_puzzle(values):
    return strategy.reduce_puzzle(values)

def search(values):
    return strategy.search(values)

def solve(grid, diagonal = True):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    if not diagonal:
        setup.deactivate_diagonal_constraints()

    result = strategy.search(util.parse_sudoku_string(grid))
    return result if result else False

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
