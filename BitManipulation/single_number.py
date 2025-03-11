# Using XOR
# Time: O(n)
# Space: O(1)
def singleNumber(nums) -> int:
    for i in range(1, len(nums)):
        nums[0] = nums[0] ^ nums[i]
    return nums[0]


print(singleNumber([4, 1, 2, 1, 2]))
