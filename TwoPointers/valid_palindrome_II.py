# Reverse + two pointers:
# Time: O(n)
# Space: O(n)
def validPalindrome(s: str) -> bool:
    start_ptr = 0
    end_ptr = len(s) - 1
    while start_ptr <= end_ptr:
        if s[start_ptr] != s[end_ptr]:
            skip_char = s[:start_ptr] + s[start_ptr + 1 :]  # Skip the char at start_ptr
            if skip_char == skip_char[::-1]:
                return True
            skip_char = s[:end_ptr] + s[end_ptr + 1 :]  # Skip the char at end_ptr
            if skip_char == skip_char[::-1]:
                return True
            return False
        start_ptr += 1
        end_ptr -= 1
    return True


# Optimal two pointers:
# Time: O(n)
# Space: O(1)
def validPalindrome(self, s: str) -> bool:
    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
        l += 1
        r -= 1

    return True


print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abc"))
