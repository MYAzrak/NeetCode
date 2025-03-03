# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# Recursive DFS:
# Time: O(n)
# Space: O(n)
def maxDepth(root) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.right), maxDepth(root.left))


# Iterative DFS:
# Time: O(n)
# Space: O(n)
def maxDepth(root) -> int:
    if not root:
        return 0

    call_stack = [[root, 1]]
    max_depth = 0

    while call_stack:
        node, depth = call_stack.pop()
        if node:
            max_depth = max(max_depth, depth)
            call_stack.append([node.left, depth + 1])
            call_stack.append([node.right, depth + 1])

    return max_depth


# Iterative BFS (level by level examination)
# Time: O(n)
# Space: O(n)
def maxDepth(root) -> int:
    if not root:
        return 0

    level = 0
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level
