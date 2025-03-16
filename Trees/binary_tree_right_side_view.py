from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS, return the last element of each level
def rightSideView(root):
    if not root:
        return []

    in_order = [[]]
    level = 0
    queue = deque([root])

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            in_order[level].append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        level += 1
        in_order.append([])

    in_order.pop()
    result = [in_order[i][-1] for i in range(len(in_order))]
    return result
