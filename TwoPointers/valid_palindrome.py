class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        return s == s[::-1]


test = Solution()
print(test.isPalindrome("race a car"))
print(test.isPalindrome("racecar"))


# NeetCode solution for better space complexity and without using isalnum()
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while l < r and not self.alphanum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     # Could write own alpha-numeric function
#     def alphanum(self, c):
#         return (
#             ord("A") <= ord(c) <= ord("Z")
#             or ord("a") <= ord(c) <= ord("z")
#             or ord("0") <= ord(c) <= ord("9")
#         )
