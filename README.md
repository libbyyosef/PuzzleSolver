# PuzzleSolver
**Overview**

This repository provides a Python implementation for solving and generating constraint puzzles using backtracking. The code is designed to work with 2D pictures where each cell can be in one of two states (0 or 1), and constraints are applied to determine the count of seen cells in each row and column.

**Code Structure**

- **solver.py:** The main module containing functions to solve and generate constraint puzzles.
  - **max_seen_cells:** Calculates the maximum number of seen cells in a given row or column.
  - **min_seen_cells:** Calculates the minimum number of seen cells in a given row or column.
  - **check_constraints:** Checks if the constraints are satisfied for a given picture.
  - **find_minus_one:** Checks if there are any unset cells in the picture.
  - **create_board:** Creates an empty picture board.
  - **seen_1:** Modifies the picture based on the constraint of having one seen cell.
  - **placed_constraints:** Initializes the picture board based on the provided constraints.
  - **solve_helper:** Recursive helper function for solving the puzzle using **backtracking** and **recursion**.
  - **solve_puzzle:** Main function to solve the constraint puzzle using backtracking.
  - **helper_solutions:** Helper function to count possible solutions for a puzzle using recursion.
  - **how_many_solutions:** Counts the total number of solutions for a puzzle.
  - **generate_puzzle:** Generates a set of constraints for a given picture.
