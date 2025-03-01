# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursively
# Time: O(N)
# Space: O(N) because of the function call stack & O(N) for res
def preorderTraversal(root):
    result = []

    def preorder(node):
        if not node:
            return
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return result


# Iteratively
# Time: O(N)
# Space: O(N)
def preorderTraversal(root):
    call_stack = []
    result = []
    curr = root

    while curr or call_stack:
        while curr:
            call_stack.append(curr)
            result.append(curr.val)
            curr = curr.left
        curr = call_stack.pop()
        curr = curr.right

    return result
