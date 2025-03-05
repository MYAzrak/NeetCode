# Recursion
# Time: O(2^n) which is the number of subsets
# Space: O(n) for recursion stack
def subsetXORSum(nums) -> int:
    # To traverse each "branch" == subset that could be obtained by nums
    def dfs(i, total):
        if i == len(nums):  # We reached the end
            return total
        return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
        #      1st child                     2nd child

    return dfs(0, 0)


# Think of it as a tree branching into 2 children each time, 1st child contains the element
# at index i and the 2nd does not. At the end of each branch we get the result of that branch
# which is a subset. E.g.:
# nums = [1, 3]. We start with an empty list.
#           {}
#       1       _
#   3   _       3   _       --> 4 subsets
