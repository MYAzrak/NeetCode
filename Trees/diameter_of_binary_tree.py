# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        result = 0

        def dfs(root) -> int:
            nonlocal result
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, left + right)
            return 1 + max(left, right)

        dfs(root)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

test = Solution()
print(test.diameterOfBinaryTree(root))
