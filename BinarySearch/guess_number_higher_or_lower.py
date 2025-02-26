# Binary search
# Time: O(log n)
# Space: O(1)
def guess(num: int) -> int:
    pick = 6
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    right = n
    left = 1
    while True:
        my_guess = (right + left) // 2
        res = guess(my_guess)
        if res == 0:
            return my_guess
        elif res == -1:
            right = my_guess - 1
        else:
            left = my_guess + 1


print(guessNumber(10))
