class Solution:
    def twoSum(self, nums, target: int):
        nums_dict = {}
        for index, num in enumerate(nums):
            if (target - num) in nums_dict.keys():
                return nums_dict[target - num], index
            nums_dict[num] = index
        return ()


test_case = Solution()
print(test_case.twoSum([2, 7, 11, 15], 9))
