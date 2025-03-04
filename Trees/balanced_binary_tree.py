# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Brute force
# Time: O(N^2)
# Space: O(N)
def isBalanced(root) -> bool:
    is_balanced = True

    def depth(node):
        if not node:
            return 0
        return 1 + max(depth(node.right), depth(node.left))

    def dfs(node):
        nonlocal is_balanced
        if node:
            depth_right = depth(node.right)
            depth_left = depth(node.left)
            if abs(depth_right - depth_left) > 1:
                is_balanced = False
                return
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return is_balanced


# DFS but starting from the bottom up to visit each node once
# Time: O(n)
# Space: O(n)
def isBalanced(root) -> bool:
    if (not root) or (not root.right and not root.left):
        return True

    def height(node):
        if not node:
            return [True, 0]

        left, right = height(node.right), height(node.left)  # Start from the end
        balanced = right[0] and left[0] and abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]

    return height(root)[0]
