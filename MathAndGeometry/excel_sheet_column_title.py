# Hint: Minus 1 from columnNumber since it would never start with 0
# Time: O(logn), it is exactly log base 26
# Space: O(1)
def convertToTitle(columnNumber: int) -> str:
    res = ""
    while columnNumber > 0:
        remainder = (columnNumber - 1) % 26  # - 1 since we are starting from 1
        res += chr(ord("A") + remainder)
        # ^ ord() gets the ASCII & chr() returns the char of the ASCII
        columnNumber = (columnNumber - 1) // 26

    # reverse since determining the rightmost char every time in the loop
    return res[::-1]
