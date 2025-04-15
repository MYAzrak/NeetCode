# Using the same idea of 'Number of 1 Bits' question
# Time: O(n)
# Space O(n)
def countBits(n: int):
    result = []

    def hammingWeight(m: int) -> int:
        ones_num = 0

        while m:
            m &= m - 1
            ones_num += 1

        return ones_num

    for i in range(n + 1):
        result.append(hammingWeight(i))

    return result


# Optimal. Since some work is repeated, we can save that to save time. e.g.
# 5 in binary is 0101 and 1 in binary is 0001 so 5 is 1 + number of 1 bits in 1
# Time: O(n)
# Space: O(n)
def countBits(n: int):
    dp = [0] * (n + 1)
    offset = 1 # Places where we change the most sig. bit. It would be [2, 4, 8, 16, 32]

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp