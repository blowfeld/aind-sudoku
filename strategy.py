from setup import *
from util import *
from collections import defaultdict
import ui

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
        the sudoku with the naked twins eliminated from units or None if the
        sudoku cannot be solved.
    """
    result = sudoku.copy()
    for unit in UNIT_LIST:
        twins = _naked_twins_in_unit(sudoku, unit)
        _remove_twin_choices(result, unit, twins)

    return result if all(len(choices) > 0 for box, choices in result.items()) else None

def _naked_twins_in_unit(sudoku, unit):
    occurrences = defaultdict(list)
    for box in unit:
        occurrences[sudoku[box]].append(box)

    return [ boxes for choices, boxes in occurrences.items()
            # ignore filled boxes, as they are covered already in 'eliminate'
            if len(choices) == len(boxes) and len(boxes) > 1 ]

def _remove_twin_choices(sudoku, unit, naked_twins):
    for box in unit:
        for twins in naked_twins:
            if len(sudoku[box]) > 1 and box not in twins:
                difference = set(sudoku[box]) - set(sudoku[next(iter(twins))])
                sudoku[box] = ''.join(sorted(difference))

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

        ui.update(result)

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

    print("Naked twins")
    sudoku = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                            'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
                            'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '379',
                            'C6': '2379', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8', 'D2': '17', 'D3': '9',
                            'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
                            'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9',
                            'F1': '4', 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                            'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345',
                            'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7', 'H2': '2', 'H3': '4', 'H4': '9',
                            'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3', 'I3': '5',
                            'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    display(sudoku)
    print("")
    display(naked_twins(sudoku))

    print("Search")
    sudoku_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    #sudoku_string = '4839.16..96734...1251.764935.81.29767295.41.81.67.82.53726.....8142....969.41..82'
    sudoku = parse_sudoku_string(sudoku_string)
    display(sudoku)
    print("")
    display(search(sudoku))
