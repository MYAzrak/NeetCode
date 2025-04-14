# Built-in function
# Time: O(1)
# Space: O(1)
def hammingWeight(n: int) -> int:
    result = 0

    for char in bin(n):
        if char == "1":
            result += 1

    return result


# Shifting to the right and checking the right-most bit if it is a 1 or 0 using % (or you
# can use &)
# Time: O(1) or specifically O(32) since n could be 32 bits
# Space: O(1)
def hammingWeight(n: int) -> int:
    result = 0

    while n:
        result += n % 2
        n = n >> 1

    return result


# This is more efferent since it would be O(number of ones in n). The trick is
# every time we minus 1 out of n we are removing a bit of value 1. However, we might
# introduce other bits of values 1 to its right --> Calculate  & n-1 to remove them.


def hammingWeight(n: int) -> int:
    result = 0

    while n:
        n &= n - 1
        result += 1

    return result


print(hammingWeight(n=11))
print(hammingWeight(n=128))
print(hammingWeight(n=2147483645))
