# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Naked twins* provides the following constraint on the choices possible in a unit:
    If a unit contains `n` boxes with identical `n` choices, this choices must
    be distributed among those `n` boxes, otherwise one of them cannot be assigned
    a value. As a consequence of that, this `n` choices can be removed from all
    other boxes in the unit. This constraint can be propagated by applying it
    repeatedly in the same way as elimination or the only choice constraint.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal sudoku problem adds two more units to the sudoku problem (namely
    the diagonals) that we need to take into account when evaluating our
    constraints. Note that we also need to take the additional units into account
    when considering the peers of a box.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a
pre-packaged Python distribution that contains all of the necessary libraries
and software for this project.  Please try using the environment provided in the
`.yaml` files in this repository.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization.
If you've followed our instructions for setting up our conda environment, you
should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using
the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
