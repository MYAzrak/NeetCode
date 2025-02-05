# Brute force
class MyHashMap:
    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key] if key in self.hashmap else -1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)


# Similar to "Design Hashset"
# Using linked lists for the keys:values inputted and an array for
# indices that point to a linked list each
# Time: O(n/k), it is O(1) according to LeetCode
# Space: O(k+m), it is O(N) according to LeetCode
# Where n is the number of keys, k is the size of the set (10000) and m is the number of unique keys.
class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.hash_map = [ListNode() for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        hashed_key = self.hash_func(key)
        head = self.hash_map[hashed_key]

        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next

        head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hashed_key = self.hash_func(key)
        head = self.hash_map[hashed_key]

        while head.next:
            if head.next.key == key:
                return head.next.value
            head = head.next

        return -1

    def remove(self, key: int) -> None:
        hashed_key = self.hash_func(key)
        head = self.hash_map[hashed_key]

        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next

    def hash_func(self, key):
        return key % len(self.hash_map)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
