# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Using a hash set
# Time: O(n)
# Space: O(n)
def hasCycle(head) -> bool:
    hash_set = set()
    while head:
        if head in hash_set:
            return True
        hash_set.add(head)
        head = head.next

    return False


# Floyd's Tortoise and Hare.
# Time: O(n)
# Space: O(1)
def hasCycle(head) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
