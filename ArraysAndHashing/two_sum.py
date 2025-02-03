# Brute force
# Time: O(N^2)
# Space: O(1)
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# Using hashmaps: We go over nums and for each num we calculate target - num and check if its in the hashmap
# Time: O(N)
# Memory: O(N)
def twoSum(nums, target):
    hashmap = {}  # num: index
    for i, num in enumerate(nums):
        if target - num in hashmap.keys():
            return [i, hashmap[target - num]]
        else:
            hashmap[num] = i


print(twoSum(nums=[2, 7, 11, 15], target=9))
print(twoSum(nums=[3, 2, 4], target=6))
print(twoSum(nums=[3, 3], target=6))
