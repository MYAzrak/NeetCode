from collections import deque


# Using BFS for each empty room
# Time: O((rows*cols)^2) in the worst case when every cell is an empty room
# Space: O(rows*cols) for the queue and visited_set
def islandsAndTreasure(grid) -> None:
    ROWS, COLS = len(grid), len(grid[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(parent_r, parent_c):
        steps_needed = 1
        visited = set()
        visited.add((parent_r, parent_c))
        queue = deque()
        queue.append([parent_r, parent_c])

        while queue:
            for _ in range(len(queue)):
                node_r, node_c = queue.popleft()

                for dr, dc in directions:
                    nei_row = node_r + dr
                    nei_col = node_c + dc
                    if (
                        0 <= nei_row < ROWS
                        and 0 <= nei_col < COLS
                        and (nei_row, nei_col) not in visited
                    ):
                        if grid[nei_row][nei_col] == 0:
                            grid[parent_r][parent_c] = steps_needed
                            return
                        elif grid[nei_row][nei_col] == -1:
                            continue
                        else:
                            queue.append((nei_row, nei_col))
                            visited.add((nei_row, nei_col))

            steps_needed += 1

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2147483647:
                bfs(r, c)


# Multi Source BFS. We are running BFS from every gate instead of every empty room and
# updating the distances each time
# Time: O(rows*cols)
# Space: O(rows*cols)


def islandsAndTreasure(grid) -> None:
    ROWS, COLS = len(grid), len(grid[0])
    queue = deque()
    visited = set()

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                queue.append((r, c))
                visited.add((r, c))

    def add_room(r, c):
        if (
            0 <= r < ROWS
            and 0 <= c < COLS
            and grid[r][c] != -1
            and (r, c) not in visited
        ):
            queue.append((r, c))
            visited.add((r, c))

    distance = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            grid[r][c] = distance
            add_room(r + 1, c)
            add_room(r - 1, c)
            add_room(r, c + 1)
            add_room(r, c - 1)
        distance += 1


grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

islandsAndTreasure(grid)

print(grid)
