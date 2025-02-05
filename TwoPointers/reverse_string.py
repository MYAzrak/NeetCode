# Built-in function
def reverseString(s) -> None:
    s.reverse()


# Using Two pointers
# Time: O(n)
# Space: O(1)
def reverseString(s) -> None:
    j = len(s) - 1
    for i in range(len(s)):
        if i >= j:
            return
        s[i], s[j] = s[j], s[i]
        j -= 1


# Using a stack
# Time: O(n)
# Space: O(n)
def reverseString(s) -> None:
    stack = []
    for char in s:
        stack.append(char)

    for i in range(len(s)):
        s[i] = stack.pop()


# Recursion
# Time: O(n)
# Space: O(n)
def reverseString() -> None:
    def reverse(l, r):
        if l < r:
            reverse(l + 1, r - 1)
            s[l], s[r] = s[r], s[l]

    reverse(0, len(s) - 1)


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)
