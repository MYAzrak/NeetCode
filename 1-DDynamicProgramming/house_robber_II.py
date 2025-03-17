# DP. As "House Robber I" but do it twice, one with the first house and without the last one
# (since they are adjacent), and one without the first and house and with the last one.
# Time: O(n)
# Space: O(1)
def rob(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    def house_robber(houses):
        rob1, rob2 = 0, 0

        for num in houses:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    return max(house_robber(nums[:-1]), house_robber(nums[1:]))
