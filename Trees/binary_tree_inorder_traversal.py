# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursively
# Time: O(N)
# Space: O(N) because of the function call stack & O(N) for res
def inorderTraversal(root):
    res = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)
    return res


# Iteratively
# Time: O(N)
# Space: O(N)
def inorderTraversal(root):
    call_stack = []
    result = []
    curr = root

    # This is doing an in-order traversal
    while curr or call_stack:
        while curr:  # Go left until null
            call_stack.append(curr)
            curr = curr.left
        # Then add it to result and go its right child
        curr = call_stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result
