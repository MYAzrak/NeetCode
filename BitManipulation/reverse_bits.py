# Shift the result left and add the least significant bit of n
# Time: O(1)
# Space: O(1)
def reverseBits(n: int) -> int:
    result = 0

    for _ in range(32):
        result = result << 1
        result += n % 2
        n = n >> 1

    return result


print(reverseBits(10100101000001111010011100))
