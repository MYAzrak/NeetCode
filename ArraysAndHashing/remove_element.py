# Two pointers
# Time: O(n)
# Space: O(1)
def removeElement(nums, val):
    k = 0  # A pointer to a num that != val
    for i in range(len(nums)):
        if nums[i] != val:
            # Similar to partition of quicksort
            nums[k] = nums[i]
            k += 1
    return k


print(removeElement(nums=[3, 2, 2, 3], val=3))
print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
