# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Iterative solution.
# Time: O(n)
# Space: O(1)
def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# Recursive solution.
# Time: O(n)
# Space: O(n)
def reverseList(head):
    if not head:  # empty
        return None

    new_head = head  # save curr head
    if head.next:  # if there is a subproblem to reverse
        new_head = reverseList(head.next)  # reverse it
        head.next.next = head  # 1 -> 2 -> None --> 1 -> 2 -> 1
    head.next = None  # --> None <- 1 <- 2

    return new_head
