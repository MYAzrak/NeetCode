from collections import deque


# Using a queue for BFS approach
# Time: O(N*M)
# Space: O(N*M)
def numIslands(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    islands_num = 0

    # Iterative BFS using a queue
    def bfs(r, c):
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        visited.add((r, c))
        queue.append((r, c))

        while queue:
            row, col = queue.popleft()  # Child's row and col

            for dr, dc in DIRECTIONS:
                modified_r = row + dr
                modified_c = col + dc
                if (
                    0 <= modified_r < ROWS
                    and 0 <= modified_c < COLS
                    and grid[modified_r][modified_c] == "1"
                    and (modified_r, modified_c) not in visited
                ):
                    queue.append((modified_r, modified_c))
                    visited.add((modified_r, modified_c))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)  # Parent's row and col
                islands_num += 1

    return islands_num


# Using DFS and marking each visited cell as '0' instead of having a visited_set
# Time: O(N*M)
# Space: O(N*M) for the call stack
def numIslands(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    islands_num = 0

    def dfs(r, c):
        if 0 <= c < COLS and 0 <= r < ROWS and grid[r][c] == "1":
            grid[r][c] = "0"  # Mark as visited
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                islands_num += 1
                dfs(r, c)

    return islands_num


print(numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
