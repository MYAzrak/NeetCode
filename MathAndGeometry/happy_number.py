# Using a hash set. There will be a loop if the answer is False.
# That's why we used a hash set to check if we go back to a number
# that we already visited
# Time: O(lne(n)) (Each iteration takes O(log n) time (as we process each digit of n))
# Space: O(log n)
def isHappy(n: int) -> bool:
    hash_set = set()
    while True:
        squared_digits = []
        for _ in range(len(str(n))):
            digit = n % 10
            n = n // 10
            squared_digits.append(digit)

        for i in range(len(squared_digits)):
            squared_digits[i] *= squared_digits[i]

        n = sum(squared_digits)
        if n == 1:
            return True
        elif n in hash_set:
            return False
        hash_set.add(n)


# print(isHappy((19)))
# print(isHappy((2)))


# Slow and fast pointers
# Time: O(log n)
# Memory O(1)
def isHappy(n: int) -> bool:
    def digits_squared_sum(n):
        squared_digits = []
        for _ in range(len(str(n))):
            digit = n % 10
            n = n // 10
            squared_digits.append(digit)

        for i in range(len(squared_digits)):
            squared_digits[i] *= squared_digits[i]

        return sum(squared_digits)

    slow, fast = n, digits_squared_sum(n)

    while True:
        if fast == 1:
            return True

        if fast == slow:
            return False

        slow = digits_squared_sum(slow)
        fast = digits_squared_sum(fast)
        fast = digits_squared_sum(fast)


print(isHappy((19)))
print(isHappy((2)))
