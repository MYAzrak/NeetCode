# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
# Time: O(size of root * size of subRoot)
# Space: O(size of root + size of subRoot)
def isSubtree(root, subRoot) -> bool:
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
    return isSubtree(root.right, subRoot) or isSubtree(root.left, subRoot)

# Same but using another helper function
def isSubtree(root, subRoot) -> bool:
    is_subtree = []

    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

    def dfs(node):
        nonlocal is_subtree
        if not node:
            return
        is_subtree.append(isSameTree(node, subRoot))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return any(is_subtree)
