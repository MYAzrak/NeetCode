# Hashmap
# Time: O(n)
# Space: O(n)
def majorityElement(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    majorityElementValue = max(hashmap.values())
    for key in hashmap:
        if hashmap[key] == majorityElementValue:
            return key


# Sorting
# Time: O(nlogn)
# Space: O(1)
def majorityElement(nums):
    nums.sort()
    majorityCount = 1
    for i in range(1, len(nums) + 1):
        if majorityCount > (len(nums) / 2):
            return nums[i - 1]
        if nums[i] == nums[i - 1]:
            majorityCount += 1
        else:
            majorityCount = 1


# Boyer Moore: Make use of the definition of "majority" (appears more than n/2 times)
# + each input must have a majority element --> if majorityCount goes below 0 then that
# num appears in less than half of the array.
# Time: O(n)
# Space: O(1)
def majorityElement(nums):
    majorityNum = majorityCount = 0
    for num in nums:
        if majorityCount == 0:
            majorityNum = num
        majorityCount += 1 if num == majorityNum else -1
    return majorityNum


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
