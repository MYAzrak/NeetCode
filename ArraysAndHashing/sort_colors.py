# Bucket Sort
# Time: O(n)
# Space: O(1)
def sortColors(nums) -> None:
    hash_map = {0: 0, 1: 0, 2: 0}

    for num in nums:
        hash_map[num] += 1

    for i in range(len(nums)):
        if hash_map[0] != 0:
            nums[i] = 0
            hash_map[0] -= 1
        elif hash_map[1] != 0:
            nums[i] = 1
            hash_map[1] -= 1
        else:
            nums[i] = 2
            hash_map[2] -= 1


# 1 Pass only. Using 3 pointers, it would be similar to partitioning in QuickSort
# Where we want everything on the right == 2, on the left == 0, and == 0 in the middle.
# Time: O(n)
# Space: O(1)
def sortColors(nums) -> None:
    l, i, r = 0, 0, len(nums) - 1

    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
        else:
            i += 1
