# Recursion
# Time: O(3^n)
# Space: O(n) for the call stack
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# Dynamic programming
# Time: O(N)
# Space: O(1)
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    one, two, three = 0, 1, 1

    for _ in range(n - 2):
        temp = three
        three = one + two + three
        one = two
        two = temp

    return three
