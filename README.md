# Sudoku Puzzle Solver

This Python program generates random Sudoku puzzles and allows users to solve them interactively. It validates user input and provides feedback on the correctness of the solution.

## Features

- Generates random Sudoku puzzles.
- Allows users to interactively solve Sudoku puzzles.
- Validates user input and provides feedback on correctness.
- Displays the solution if the user fails to solve the puzzle after three attempts.

## Usage

1. Run the `sudoku_solver.py` script in a Python environment.
2. Follow the prompts to input numbers into the Sudoku grid.
3. Input `0` to exit the game.
4. If the user fails to solve the puzzle after three attempts, the solution is displayed.

## Files

- `sudoku_solver.py`: Main Python script containing the Sudoku solving logic.
- `README.md`: Documentation file providing an overview of the program and instructions for usage.

## Dependencies

- Python 3.x

## Example

```shell
$ python sudoku_solver.py
Randomly Generated Sudoku Puzzle:
   1 2 3   4 5 6   7 8 9
1 | 6 7 _ | 8 _ _ | _ 4 5 |
2 | _ 5 8 | 1 _ _ | _ _ _ |
3 | _ _ _ | _ _ _ | _ _ _ |
   ---------------------
4 | _ _ _ | _ _ _ | _ _ _ |
5 | _ _ _ | _ _ _ | _ _ _ |
6 | _ _ _ | _ _ _ | _ _ _ |
   ---------------------
7 | _ _ _ | _ _ _ | _ _ _ |
8 | _ _ _ | _ _ _ | _ _ _ |
9 | _ _ _ | _ _ _ | _ _ _ |
Enter row (1-9), column (1-9), and number (1-9) or 0 to exit: 1 3 3
Updated Sudoku Puzzle:
   1 2 3   4 5 6   7 8 9
1 | 6 7 3 | 8 _ _ | _ 4 5 |
2 | _ 5 8 | 1 _ _ | _ _ _ |
3 | _ _ _ | _ _ _ | _ _ _ |
   ---------------------
4 | _ _ _ | _ _ _ | _ _ _ |
5 | _ _ _ | _ _ _ | _ _ _ |
6 | _ _ _ | _ _ _ | _ _ _ |
   ---------------------
7 | _ _ _ | _ _ _ | _ _ _ |
8 | _ _ _ | _ _ _ | _ _ _ |
9 | _ _ _ | _ _ _ | _ _ _ |
Enter row (1-9), column (1-9), and number (1-9) or 0 to exit: 0 0 0
Three wrong attempts. Showing the solution:
   1 2 3   4 5 6   7 8 9
1 | 6 7 9 | 8 3 2 | 1 4 5 |
2 | 3 5 8 | 1 4 7 | 2 9 6 |
3 | 1 2 4 | 6 9 5 | 7 8 3 |
   ---------------------
4 | 2 1 6 | 3 7 9 | 5 3 4 |
5 | 5 9 3 | 4 8 1 | 6 2 7 |
6 | 4 8 7 | 5 2 6 | 9 1 8 |
   ---------------------
7 | 7 6 1 | 9 5 3 | 8 7 2 |
8 | 9 4 5 | 7 1 8 | 3 6 9 |
9 | 8 3 2 | 6 4 9 | 4 5 1 |
Congratulations! You solved the Sudoku puzzle. You are the winner!
