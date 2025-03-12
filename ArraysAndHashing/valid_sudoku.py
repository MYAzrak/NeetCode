from collections import defaultdict


# Hash set (one pass). We make a hash set for each row, col, and square and store them
# in 3 dictionaries where the keys are rows and cols indices
# For each 3*3 square, we divide each index by 3 (int division) which makes the whole
# 9*9 board seems as a 3*3 board with each 'cell' being a square on its own.
def isValidSudoku(board) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True
