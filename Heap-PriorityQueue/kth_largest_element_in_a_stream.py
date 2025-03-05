import heapq


# Using Min Heap if size k
# Time: O(logn) for constructor
# & O(nlogn) for add() since adding and popping from heaps is logn and we do (n-k) pops in the beginning
# Space: O(n)
class KthLargest:
    def __init__(self, k: int, nums):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) # Pops the smallest element
        return self.min_heap[0]
