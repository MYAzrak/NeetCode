from collections import deque


# Using a queue for BFS approach and creating a dictionary that contains
# key:value as island_num: list of cells that creates it
# Time: O(N*M)
# Space: O(N*M)
def maxAreaOfIsland(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    islands = {}
    island_num = 0
    visited = set()

    def bfs(r, c, island_num):
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        queue.append((r, c))

        while queue:
            child_r, child_c = queue.popleft()
            for dr, dc in DIRECTIONS:
                modified_r, modified_c = child_r + dr, child_c + dc
                if (
                    0 <= modified_r < ROWS
                    and 0 <= modified_c < COLS
                    and grid[modified_r][modified_c] == 1
                    and (modified_r, modified_c) not in visited
                ):
                    visited.add((modified_r, modified_c))
                    queue.append((modified_r, modified_c))
                    islands[island_num].append((modified_r, modified_c))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                islands[island_num] = [(r, c)]
                bfs(r, c, island_num)
                island_num += 1

    result = 0
    for cells in islands.values():
        result = max(result, len(cells))

    return result


# Using DFS and marking each visited cell as '0' instead of having a visited_set
# Time: O(N*M)
# Space: O(N*M) for the call stack
def maxAreaOfIsland(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    islands = {}
    island_num = 0

    def dfs(r, c, island_num):
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
            islands[island_num].append((r, c))
            grid[r][c] = 0
            dfs(r - 1, c, island_num)
            dfs(r + 1, c, island_num)
            dfs(r, c - 1, island_num)
            dfs(r, c + 1, island_num)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                islands[island_num] = []
                dfs(r, c, island_num)
                island_num += 1

    result = 0
    for cells in islands.values():
        result = max(result, len(cells))

    return result


# Using DFS and marking each visited cell as '0' instead of having a visited_set
# and without using a dictionary since you can return 1 + dfs()... for each cell
# Time: O(N*M)
# Space: O(N*M) for the call stack
def maxAreaOfIsland(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c):
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        return 0

    result = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                result = max(result, dfs(r, c))

    return result


print(
    maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)
