# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursion. When there is a split then that's the LCA or if the curr_node == p or q val
# Time: O(h) which would be O(n) in case of skewed tree
# Space: O(h)
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val > q.val:
        p, q = q, p

    lca = TreeNode()

    def dfs(node):
        nonlocal lca
        if not root:
            return

        if node.val == p.val or node.val == q.val:
            lca = node
            return

        if node.val > p.val and node.val < q.val:
            lca = node
            return

        if node.val > p.val and node.val > q.val:
            dfs(node.left)

        if node.val < p.val and node.val < q.val:
            dfs(node.right)

    dfs(root)
    return lca


# Iteration
# Time: O(h)
# Space: O(1)
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val > q.val:
        p, q = q, p

    while root:
        if root.val == p.val or root.val == q.val:
            return root

        if root.val > p.val and root.val < q.val:
            return root

        if root.val > p.val and root.val > q.val:
            root = root.left

        if root.val < p.val and root.val < q.val:
            root = root.right
