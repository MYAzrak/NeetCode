# Binary search
# Time: O(log n)
# Space: O(1)
def searchInsert(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right + 1

print(searchInsert([2], 1))
