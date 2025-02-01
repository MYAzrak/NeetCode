from collections import Counter


# Using Python features
def containsDuplicate(nums):
    return any(num != 1 for num in Counter(nums).values())


# Brute force
# Time: O(n^2)
# Space: O(1)
def containsDuplicate(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# With sorting
# Time: O(nlogn) which is the cost of sorting
# Space: O(1)
def containsDuplicate(nums):
    n = len(nums)
    nums.sort()
    for i in range(0, n - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# With a hash set
# Time: O(n)
# Space: O(n)
def containsDuplicate(nums):
    hash_set = set()
    for n in nums:
        if n in hash_set:
            return True
        hash_set.add(n)
    return False


print(containsDuplicate([1, 1, 2, 3, 4, 5, 6]))
