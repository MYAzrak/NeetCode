from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Use a hashmap to save old:new nodes and use DFS to clone recursively
# Time: O(N+E)
# Space: O(N)
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        old_to_new = {}  # Tracks the old nodes to their deep copied versions
        # This is to help us append deep copied neighbors

        def dfs(old):
            if old in old_to_new:
                return old_to_new[old]

            new = Node(old.val)
            old_to_new[old] = new
            for neighbor in old.neighbors:
                new.neighbors.append(dfs(neighbor))
            return new

        return dfs(node)
