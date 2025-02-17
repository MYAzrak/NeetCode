# Using a sliding window and a hash set
# Time: O(N)
# Space: O(N)
def containsNearbyDuplicate(nums, k: int) -> bool:
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L > k: # Sliding window
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False


print(containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
print(containsNearbyDuplicate(nums=[99, 99], k=2))
