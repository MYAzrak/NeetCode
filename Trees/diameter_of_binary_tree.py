# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root) -> int:
    result = 0

    # Returns the height
    def dfs(node) -> int:
        nonlocal result  # meaning that it is the same variable `result` before this function
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        result = max(result, left + right)
        return 1 + max(left, right)

    dfs(root)
    return result
