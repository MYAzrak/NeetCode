# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    # Recursive DFS: O(n), O(n)
    # def maxDepth(self, root) -> int:
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    # Iterative BFS (level by level examination): O(n), O(n)
    # def maxDepth(self, root) -> int:
    #     if not root:
    #         return 0

    #     level = 0
    #     queue = deque([root])
    #     while queue:
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         level += 1
    #     return level

    # Iterative DFS: O(n), O(n)
    def maxDepth(self, root) -> int:
        stack = [[root, 1]]
        max_depth = 1
        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return max_depth
