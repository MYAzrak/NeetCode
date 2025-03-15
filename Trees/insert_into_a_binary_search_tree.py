# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iteration
# Time: O(h)
# Space: O(1)
def insertIntoBST(root, val: int):
    if not root:
        root = TreeNode(val)
        return root

    curr = root
    prev = None
    direction = ""

    while curr:
        prev = curr
        if curr.val > val:
            curr = curr.left
            direction = "LEFT"
        else:
            curr = curr.right
            direction = "RIGHT"

    if direction == "LEFT":
        prev.left = TreeNode(val)
    else:
        prev.right = TreeNode(val)

    return root

# Recursion