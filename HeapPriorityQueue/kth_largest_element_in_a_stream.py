import heapq


class KthLargest:
    def __init__(self, k: int, nums):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k: 
            heapq.heappop(self.min_heap)  # Pops the smallest element

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
test = KthLargest(3, [4, 5, 8, 2])
print(test.add(3))  # return 4
print(test.add(5))  # return 5
print(test.add(10))  # return 5
print(test.add(9))  # return 8
print(test.add(4))  # return 8
