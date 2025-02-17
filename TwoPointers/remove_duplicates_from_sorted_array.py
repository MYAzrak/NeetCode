# Using sort
# Time: O(n)
# Space: O(1)
def removeDuplicates(nums) -> int:
    curr = nums[0]
    k = 1
    for i in range(1, len(nums)):
        if nums[i] == curr:
            nums[i] = 101
        else:
            curr = nums[i]
            k += 1
    nums.sort()
    print(nums)
    return k


# print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(removeDuplicates(nums=[1, 1, 2]))


# Using two pointers
# Time: O(n)
# Space: O(1)
def removeDuplicates(nums) -> int:
    r = 1
    l = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[l] = nums[i]
            l += 1
        r += 1
    return l

print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates(nums=[1, 1, 2]))
