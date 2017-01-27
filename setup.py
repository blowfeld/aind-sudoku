def _cross(a, b):
    "cross product of elements in A and elements in B."
    return [ s + t for s in a for t in b ]

ROWS = 'ABCDEFGHI'
COLS = '123456789'

BOXES = _cross(ROWS, COLS)

ROW_UNITS = [_cross(r, COLS) for r in ROWS]
COLUMN_UNITS = [_cross(ROWS, c) for c in COLS]
BOX_UNITS = [_cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
DIAGONAL_UNITS = [[a + b for a, b in zip(ROWS, COLS)], [a + b for a, b in zip(ROWS, COLS[::-1])]]

UNIT_LIST = ROW_UNITS + COLUMN_UNITS + BOX_UNITS + DIAGONAL_UNITS
UNITS = dict((s, [u for u in UNIT_LIST if s in u]) for s in BOXES)
PEERS = dict((s, set(sum(UNITS[s], [])) - set([s])) for s in BOXES)

def deactivate_diagonal_constraints():
    global UNIT_LIST, UNITS, PEERS

    UNIT_LIST = ROW_UNITS + COLUMN_UNITS + BOX_UNITS
    UNITS = dict((s, [u for u in UNIT_LIST if s in u]) for s in BOXES)
    PEERS = dict((s, set(sum(UNITS[s], [])) - set([s])) for s in BOXES)


if __name__ == '__main__':
    from pprint import pprint

    pprint("ROWS")
    pprint(ROWS)
    pprint("COLS")
    pprint(COLS)
    pprint("BOXES")
    pprint(BOXES)
    pprint("ROW_UNITS")
    pprint(ROW_UNITS)
    pprint("COLUMN_UNITS")
    pprint(COLUMN_UNITS)
    pprint("BOX_UNITS")
    pprint(BOX_UNITS)
    pprint("DIAGONAL_UNITS")
    pprint(DIAGONAL_UNITS)
    pprint("UNIT_LIST")
    pprint(UNIT_LIST)
    pprint("UNITS")
    pprint(UNITS)
    pprint("UNITS")
    pprint("PEERS")
    pprint(PEERS)
