# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(size of root * size of subRoot)
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def is_same_tree(root, sub_root):
            if not root and not sub_root:
                return True
            if not root or not sub_root or root.val != sub_root.val:
                return False
            return is_same_tree(root.right, sub_root.right) and is_same_tree(
                root.left, sub_root.left
            )

        if not subRoot:
            return True
        if not root:
            return False
        if is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


test = Solution()

root = TreeNode(3)
root.right = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

sub_root = TreeNode(4)
sub_root.right = TreeNode(2)
sub_root.left = TreeNode(1)

print(test.isSubtree(root, sub_root))
