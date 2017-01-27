from setup import *
from util import *
from collections import defaultdict
import display

def eliminate(sudoku):
    """
    Eliminate peer values from the choices in the provided sudoku.
    Input: A sudoku in dictonary form, mapping boxs to the possible values.
            Keys: The boxes, e.g., 'A1'
            Values: choices for the values in the box, e.g., '238'.
    Output: The sudoku in dictionary form after elimination or None if the sudoku
            cannot be solved
    """
    filled_boxes = { k: v for k, v in sudoku.items() if len(v) == 1 }

    result = sudoku.copy()
    for box, choice in filled_boxes.items():
        for peer in PEERS[box]:
            new_choices = result[peer].replace(choice, '')
            if len(new_choices) == 0:
                return None
            result[peer] = new_choices

    return result

def only_choice(sudoku):
    """
    Select unique choices in the provided sudoku.
    Input: A sudoku in dictonary form, mapping boxs to the possible values.
            Keys: The boxes, e.g., 'A1'
            Values: choices for the values in the box, e.g., '238'.
    Output: The sudoku in dictionary form after selection
    """
    result = sudoku.copy()
    for unit in UNIT_LIST:
        result.update(_only_choices_in_unit(sudoku, unit))

    return result

def _only_choices_in_unit(sudoku, unit):
    occurrences = defaultdict(list)
    for box in unit:
        for choice in sudoku[box]:
            occurrences[choice].append(box)

    return { boxes[0]: choice for choice, boxes in occurrences.items() if len(boxes) == 1 }

def naked_twins(sudoku):
    """Eliminate values using the naked twins strategy.
    Args:
        sudoku(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def search(sudoku):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    reduced = reduce_sudoku(sudoku)
    if not reduced:
        return None

    unfilled = [ (k, v) for k, v in reduced.items() if len(v) > 1 ]
    if not unfilled:
        return reduced

    box, choices = min(unfilled, key = lambda val: len(val[1]))
    for choice in choices:
        attempt = reduced.copy()
        attempt[box] = choice
        result = search(attempt)
        if result:
            return result

    return None

def reduce_sudoku(sudoku):
    """
    Recursively apply the eliminate and only_choice strategies.
    If at some point, there is a box with no available values, terminate.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form or None if the sudoku is not solvable.
    """
    result = sudoku.copy()

    stalled = False
    while not stalled:
        solved_boxes_before = len([box for box in result.keys() if len(result[box]) == 1])

        result = eliminate(result)
        result = only_choice(result) if result else None
        if not result or len([box for box in result.keys() if len(result[box]) == 0]):
            return None

        display.update(result)

        solved_boxes_after = len([box for box in result.keys() if len(result[box]) == 1])
        stalled = solved_boxes_before == solved_boxes_after

    return result


if __name__ == '__main__':
    from pprint import pprint

    print("eliminate")
    sudoku_string = '4839216579673458212518764935.81.29767295.41.81.67.82.5372689514814253769695417382'
    #sudoku_string = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
    sudoku = parse_sudoku_string(sudoku_string)
    display(sudoku)
    print("")
    display(eliminate(sudoku))

    print("Only choice")
    sudoku_string = '4839216579673458212518764935.81.29767295.41.81.67.82.5372689514814253769695417382'
    sudoku = eliminate(parse_sudoku_string(sudoku_string))
    display(sudoku)
    print("")
    display(only_choice(sudoku))

    print("Search")
    sudoku_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    #sudoku_string = '4839.16..96734...1251.764935.81.29767295.41.81.67.82.53726.....8142....969.41..82'
    sudoku = parse_sudoku_string(sudoku_string)
    display(sudoku)
    print("")
    display(search(sudoku))
