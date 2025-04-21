# This could be solved using sorting or a hash set.
# But the most eff way is using XOR or sum.
# Time: O(n)
# Space: O(1)
def missingNumber(nums) -> int:
    xor = len(nums)

    for i in range(len(nums)):
        xor ^= i ^ nums[i]

    return xor


def missingNumber(nums) -> int:
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]

    return res
