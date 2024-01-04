#!/usr/bin/python3
"""N Queens Module."""

import sys


def solve_nqueens(board, col, n, solutions):
    """Recursively solve the N Queens problem."""
    if col == n:
        # Found a solution, add it to the list of solutions
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if (board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0
