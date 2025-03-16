# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 3 cases when we reach the keyNode: 1- it has a right only --> return right
# 2- left only --> return left 3- has both --> find the min val of its right subtree and
# swap their vals call deleteNode on keyNode.right with the min.val as key
# Time: O(h)
# Space: O(h)
def deleteNode(root, key: int):
    if not root:
        return

    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        root_right_min = root.right
        while root_right_min.left:
            root_right_min = root_right_min.left
        root.val = root_right_min.val
        root.right = deleteNode(root.right, root_right_min.val)

    return root
