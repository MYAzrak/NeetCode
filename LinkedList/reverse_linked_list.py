# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Iterative solution, O(n), O(1)
class Solution:
    def reverseList(self, head):
        prev, current = None, head

        while current:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next

        return prev


# Recursive solution, O(n), O(n)
class Solution:
    def reverseList(self, head):
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head
