# DFS Recursion. Get the max b/w robbing house[0] and max(houses[0+2] until the end)
# and max(all houses skipping house 0)
# Time: O(2^n)
# Space: O(n)
def rob(nums) -> int:
    def dfs(i):
        if i >= len(nums):
            return 0

        return max(dfs(i + 1), nums[i] + dfs(i + 2))

    return dfs(0)


# DP (Top-Down from a decision tree) starting from the first house until the end, some
# 'subtrees' are duplicated --> save their values in a memoization list
# Time: O(n)
# Space: O(n)
def rob(nums) -> int:
    memo = [-1] * len(nums)

    def dfs(i):
        if i >= len(nums):
            return 0

        if memo[i] != -1:
            return memo[i]

        memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

        return memo[i]

    return dfs(0)


# DP (Space optimized). For each num, get max (prev subarr, or num + prev subarr not including
# last element), then advance rob1 and rob2
def rob(nums) -> int:
    # [rob1, rob2, num, num+1...]
    rob1, rob2 = 0, 0

    for num in nums:
        temp = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2
