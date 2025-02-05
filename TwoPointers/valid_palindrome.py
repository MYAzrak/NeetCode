# Using reverse
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        return s == s[::-1]


# Two pointers
# Time: O(n)
# Space: O(1)
def isPalindrome(s: str) -> bool:
    start_ptr = 0
    end_ptr = len(s) - 1
    while start_ptr < end_ptr:
        if not s[start_ptr].isalnum():
            start_ptr += 1
            continue

        if not s[end_ptr].isalnum():
            end_ptr -= 1
            continue

        if s[start_ptr].lower() != s[end_ptr].lower():
            return False
        else:
            start_ptr += 1
            end_ptr -= 1
    return True


print(isPalindrome("race a car"))
print(isPalindrome("racecar"))
print(isPalindrome(" "))
print(isPalindrome("A man, a plan, a canal: Panama"))
