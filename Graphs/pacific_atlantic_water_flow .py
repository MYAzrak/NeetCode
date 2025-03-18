# DFS where we start from water to land instead of land to water. Make a set for
# pacific and atlantic first test which cells can reach atlantic then pacific
# instead of a nested for loop for each cell
# Time: O(M*N)
# Space: O(M*N)
def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prev_height):
        if (
            (r, c) in visited
            or r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or heights[r][c] < prev_height
        ):
            return

        visited.add((r, c))
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pacific, heights[0][c])
        dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pacific and (r, c) in atlantic:
                res.append([r, c])

    return res
