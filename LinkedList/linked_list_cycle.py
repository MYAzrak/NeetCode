# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time: O(n). Space: O(n)
class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False

        my_hash = set()
        while head.next:
            if head in my_hash:
                return True
            my_hash.add(head)
            head = head.next

        return False


# Floyd's Tortoise and Hare. Time: O(n). Space: O(1)
class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
