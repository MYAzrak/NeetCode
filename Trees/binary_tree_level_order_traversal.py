from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
# Time: O(N)
# Space: O(N)
def levelOrder(root):
    if not root:
        return []

    result = [[]]
    level = 0
    queue = deque([root])

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            result[level].append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
        result.append([])

    result.pop()
    return result


# DFS
# Time: O(N)
# Space: O(N)
def levelOrder(root):
    if not root:
        return []

    res = [[]]

    def dfs(node, level):
        if not node:
            return
        if len(res) == level:
            res.append([])

        res[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return res
