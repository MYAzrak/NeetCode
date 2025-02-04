# Brute force
# Time: O(n) for each function
# Space: O(n)
class MyHashSet:
    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashSet


# Using linked lists for the values (keys) inputted and an array for
# indices that point to a linked list each
# Time: O(n/k)
# Space: O(k+m)
# Where n is the number of keys, k is the size of the set (10000) and m is the number of unique keys.
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        # The size is specified in the question
        # Initialize each with a dummy node to make handling edge cases easier
        self.hashSet = [ListNode(0) for _ in range(10**4)]
        # self.hashSet = [ListNode(0)] * 10**4 # This is a bug, this copies the same ListNode(0) and doesn't make a new ListNode for each

    def add(self, key: int) -> None:
        index = self.hashFunc(key)
        head = self.hashSet[index]

        while head.next:
            # head.next.key to skip the dummy node in the beginning
            if head.next.key == key:
                return
            head = head.next  # To move to the linked list's end

        head.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hashFunc(key)
        head = self.hashSet[index]

        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next

    def contains(self, key: int) -> bool:
        index = self.hashFunc(key)
        head = self.hashSet[index]

        while head.next:
            if head.next.key == key:
                return True
            head = head.next

        return False

    # A simple hash function
    def hashFunc(self, key):
        return key % len(self.hashSet)


myHashSet = MyHashSet()
myHashSet.add(1)  # set = [1]
myHashSet.add(2)  # set = [1, 2]
myHashSet.contains(1)  # return True
myHashSet.contains(3)  # return False, (not found)
myHashSet.add(2)  # set = [1, 2]
myHashSet.contains(2)  # return True
myHashSet.remove(2)  # set = [1]
myHashSet.contains(2)  # return False, (already removed)
