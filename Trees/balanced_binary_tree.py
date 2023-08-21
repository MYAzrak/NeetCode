# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        if (not root) or (not root.right and not root.left):
            return True

        def height(root):
            if not root:
                return [True, 0]

            left, right = height(root.right), height(root.left)
            balanced = right[0] and left[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return height(root)[0]


test = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(test.isBalanced(root))
