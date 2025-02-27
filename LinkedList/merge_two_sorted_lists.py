# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Space: O(1)
def mergeTwoLists(list1, list2):
    sorted_list = ListNode()
    head = sorted_list

    while list1 and list2:
        if list1.val > list2.val:
            sorted_list.next = list2
            list2 = list2.next
        else:
            sorted_list.next = list1
            list1 = list1.next
        sorted_list = sorted_list.next

    if list1:
        sorted_list.next = list1
    elif list2:
        sorted_list.next = list2

    return head.next
