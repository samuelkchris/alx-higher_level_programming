#!/usr/bin/python3

import sys

def nqueens(n):
    def is_valid(queens, row, col):
        for q in queens:
            if q[1] == col or q[0] - q[1] == row - col or q[0] + q[1] == row + col:
                return False
        return True

    def solve(queens, row):
        if row == n:
            return queens
        for col in range(n):
            if is_valid(queens, row, col):
                queens.append((row, col))
                solution = solve(queens, row + 1)
                if solution is not None:
                    return solution
                queens.pop()
        return None

    queens = solve([], 0)
    if queens is None:
        return []
    return queens

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)

solutions = nqueens(n)
for solution in solutions:
    print(solution)
