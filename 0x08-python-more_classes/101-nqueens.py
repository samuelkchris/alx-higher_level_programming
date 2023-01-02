#!/usr/bin/python3
'''Module for N Queens problem.'''


def isSafe(board, row, col):
    '''Checks if position is safe from attack.
    Args:
        board: The board state.
        row: The row to check.
        col: The colum to check.
    '''
    for c in range(col):
        if board[c] is row or abs(board[c] - row) is abs(c - col):
            return False
    return True


def checkBoard(board, col):
    '''Checks the board state column by column using backtracking.
    Args:
        board: The board state.
        col: The current colum to check.
    '''
    n = len(board)
    if col is n:
        print(str([[c, board[c]] for c in range(n)]))
        return

    for row in range(n):
        if isSafe(board, row, col):
            board[col] = row
            checkBoard(board, col + 1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = 0
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(n)]
    checkBoard(board, 0)
