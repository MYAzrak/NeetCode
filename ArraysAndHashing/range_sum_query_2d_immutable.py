# Go back to the video if you do not understand this
# Two Dimensional Prefix Sum
# Time: O(n^2) for the constructor and O(1) for sumRegion()
# Space: O(n^2)
class NumMatrix:
    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])

        # Calculating this is O(N^2) but then every call to sumRegion would be O(1).
        # We are adding an additional col and row to help us with the edge case where
        # the row or col that we want to minus is out of bounds.
        self.prefix_matrix = [[0] * (COLS + 1) for row in range(ROWS + 1)]

        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                above = self.prefix_matrix[row][col + 1]
                self.prefix_matrix[row + 1][col + 1] = prefix + above
                # ^ + above since 2D

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Add offset that we added to the prefix_matrix
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # You need a drawing to understand this. The key concept is that every bottom_right
        # cell contains the sum of the big matrix that it creates from 0,0 until row2,col2
        bottom_right = self.prefix_matrix[row2][col2]
        above = self.prefix_matrix[row1 - 1][col2]
        left = self.prefix_matrix[row2][col1 - 1]
        top_left = self.prefix_matrix[row1 - 1][col1 - 1]
        return bottom_right - above - left + top_left
