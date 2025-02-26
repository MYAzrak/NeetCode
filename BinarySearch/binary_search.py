# Binary search
# Time: O(log n) since we dividing the solution space by 2 each time 
# Space: O(1)
def search(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        # mid = left + (right - left) // 2 # You can use this to prevent overflow in languages that have overflow
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))
