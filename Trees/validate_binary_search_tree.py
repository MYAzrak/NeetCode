from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Going over each node and each other node to check the BST properties
# Time: O(N^2)
# Space: O(N)
def isValidBST(root) -> bool:
    if not root:
        return True

    def dfs(node, is_left_check, parent_val):
        if is_left_check:
            if node.val >= parent_val:
                return False
        else:
            if node.val <= parent_val:
                return False

        if node.right:
            if not dfs(node.right, is_left_check, parent_val):
                return False
        if node.left:
            if not dfs(node.left, is_left_check, parent_val):
                return False

        return True

    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr.right:
                queue.append(curr.right)
                if not dfs(curr.right, False, curr.val):
                    return False

            if curr.left:
                queue.append(curr.left)
                if not dfs(curr.left, True, curr.val):
                    return False

    return True


# Make a min_limit, max_limit and update it as you traverse the tree. When going to the right
# every node should be larger than the parent --> update the min to parent.val when going to
# the right, and update max when going to the left.
# Time: O(N)
# Space: O(N)
def isValidBST(root) -> bool:
    def valid(node, left, right):
        if not node:
            return True

        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))
