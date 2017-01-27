"""
This module provides a workaround to make the visualize accessible from modules
outside of solution.py.
"""

updates = None

def update(sudoku):
    if updates is not None and sudoku:
        updates.append(sudoku.copy())
