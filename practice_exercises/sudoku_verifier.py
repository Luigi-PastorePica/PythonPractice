"""
You have a filled sudoku grid, represented by an array, where each element is a row represented by an array of integers.
Remember that sudoku is an n x n grid (usually 9 x 9) where:
- each row contains all the numbers from 1 to 9 without repetition.
- each column contains all the numbers from 1 to 9 without repetition.
- In addition, the grid is subdivided in 9 sub-grids of 9 by 9 each. Each sub-grid contains all the numbers from 1 to 9
without repetition.

Write a function that takes in the solved sudoku and outputs the following:
- If a row is invalid, return "row <n> invalid".
- If a column is invalid, return "column <m> invalid".
- If a region is invalid, return "region <r> invalid".

Where n is the row number, m is the column number, and r is the region number.
"""