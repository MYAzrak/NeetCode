# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
# class Solution:
#     def isSameTree(self, p, q) -> bool:
#         if not p and not q:
#             return True
#         elif not p and q:
#             return False
#         elif p and not q:
#             return False
#         elif p.val != q.val:
#             return False
#         my_list1 = []
#         my_list2 = []
#         my_list1.append(self.isSameTree(p.right, q.right))
#         my_list2.append(self.isSameTree(p.left, q.left))
#         if False in my_list1 or False in my_list2:
#             return False
#         return True


test = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# p = TreeNode(1)
# p.left = TreeNode(2)

# q = TreeNode(1)
# q.right = TreeNode(2)
print(test.isSameTree(p, q))
