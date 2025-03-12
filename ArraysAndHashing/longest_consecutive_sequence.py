# Sorting
# Time: O(nlogn)
# Space: O(1)
def longestConsecutive(nums) -> int:
    if not nums:
        return 0

    result = 1
    nums.sort()

    temp_max = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] == nums[i - 1] + 1:
            temp_max += 1
        else:
            result = max(result, temp_max)
            temp_max = 1

    return max(result, temp_max)


# Using a hash set and do a lookup (which is O(1)) to check for sequences' starting
# numbers which have the characteristic (num - 1) not in nums. Then we
# build that sequence until the end and save its length and do the same for
# all sequences and return the largest length.
# Time: O(n)
# Space: O(n)
def longestConsecutive(nums) -> int:
    nums = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) not in nums:
            length = 1
            while (num + length) in nums:
                length += 1
            longest = max(length, longest)
    return longest


print(longestConsecutive([0, -1]))
