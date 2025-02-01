# With Python features
# def getConcatenation(nums):
# return nums + nums


def getConcatenation(nums):
    ans = []
    for _ in range(2):
        for num in nums:
            ans.append(num)
    return ans


# With a single iteration
def getConcatenation(nums):
    nums_length = len(nums)
    ans = [0] * 2 * nums_length

    for i, num in enumerate(nums):
        ans[i] = ans[i + nums_length] = num

    return ans


print(getConcatenation([1, 2, 3]))
# Time complexity: O(n) or precisely O(n + n) here
# Space complexity: Same as time
