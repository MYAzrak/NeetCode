# Binary search
# Time: O(log n)
# Space: O(1)
def mySqrt(x: int) -> int:
    left = 0
    right = x
    while True:
        mid = left + ((right - left) // 2)
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            if (mid - 1) * (mid - 1) < x:
                return mid - 1
            else:
                right = mid - 1
        elif mid * mid < x:
            if (mid + 1) * (mid + 1) > x:
                return mid
            else:
                left = mid + 1


# Brute force
# Time: O(sqrt(n)) since we know it is the sqrt(x)
# Space: O(1)
def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    res = 1
    for i in range(1, x + 1):
        if i * i > x:
            return res
        res = i

    return res
