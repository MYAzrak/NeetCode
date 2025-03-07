# Recursion similar to Sum Of All Subsets XOR Total
# Time: O(2^n)
# Space: O(n)
def climbStairs(n: int) -> int:
    def dfs(i):
        if i >= n:
            return i == n
        return dfs(i + 1) + dfs(i + 2)

    return dfs(0)


# Dynamic Programming (Bottom-Up)
# E.g.  S1  S2  S3  S4  S5
# The idea is that we start from the last step and go back. If we start from the
# last step, how many ways can we get to the last step? Ans: Only by not moving  so 1
# (think of it as n=1).Then in the step before it, how many ways can we get to the end?
# Only by moving 1 step and not 2 so Ans: 1. Then in S3, we calculate the ways we can
# reach the end from S4 & S5 since from S3 we can only get to S4 & S5 (Ans: 1 + 1 here).
# This is similar to Fib seq but fib(n+1). The final answer would be at S0 (i.e on the floor).
# Time: O(N)
# Space: O(1)
def climbStairs(n: int) -> int:
    one, two = 1, 1

    for _ in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


print(climbStairs(8))
