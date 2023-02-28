#!/usr/bin/python3
"""solving the N queens problem"""

import sys

numQueens = 4
currentSolution = [0 for x in range(numQueens)]
solutions = []


def isSafe(testRow, testCol):
    """function to test whether a column and row is safe for a queen"""
    if testRow == 0:
        return True

    for row in range(0, testRow):
        """check vertical"""
        if testCol == currentSolution[row]:
            return False

        """check diagonal"""
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False
    """no attack"""
    return True


def placeQueen(row):
    """for general number of queens"""
    global currentSolution, solutions, numQueens

    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col
            if row == (numQueens - 1):
                """lastrow"""
                solutions.append(currentSolution.copy())
            else:
                placeQueen(row + 1)


placeQueen(0)


def make_all_boards(res):
    """Method that builts the List that be returned"""
    actual_boards = []
    for numQueens in res:
        board = []
        for row, col in enumerate(numQueens):
            board.append([row, col])
        actual_boards.append(board)
    return actual_boards


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
