# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursively
# Time: O(N)
# Space: O(N) because of the function call stack & O(N) for res
def postorderTraversal(root):
    result = []

    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result.append(node.val)

    postorder(root)
    return result


# Iteratively where we do val -> right -> left then reverse which is easier than
# having a is_visited list to check if its the second time visiting a node
# Time: O(N)
# Space: O(N)
def postorderTraversal(root):
    call_stack = []
    result = []
    curr = root

    while curr or call_stack:
        while curr:
            result.append(curr.val)
            call_stack.append(curr)
            curr = curr.right
        curr = call_stack.pop()
        curr = curr.left

    result.reverse()
    return result
