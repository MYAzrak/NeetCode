# Brute force
# Time: O(N * M)
# Space: O(1)
def islandPerimeter(grid) -> int:
    perimeter = 0
    cols_num = len(grid[0])
    rows_num = len(grid)

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 1:
                cell_perimeter = 4
                if col_index - 1 >= 0 and grid[row_index][col_index - 1] == 1:
                    cell_perimeter -= 1
                if col_index + 1 < cols_num and grid[row_index][col_index + 1] == 1:
                    cell_perimeter -= 1
                if row_index - 1 >= 0 and grid[row_index - 1][col_index] == 1:
                    cell_perimeter -= 1
                if row_index + 1 < rows_num and grid[row_index + 1][col_index] == 1:
                    cell_perimeter -= 1
                perimeter += cell_perimeter

    return perimeter


print(islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
